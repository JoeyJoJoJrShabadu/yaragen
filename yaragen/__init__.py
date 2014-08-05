import pkgutil
from importlib import import_module
from collections import OrderedDict
import yara

import ruletypes
from rulegens import BinaryGen, HeaderGen

# Should we define this or autopopulate??
GENCLASSES = [BinaryGen, HeaderGen]

def is_ruletype(rule):
    """ Helper function used to ensure only rule classes are being returned"""
    try:
        getattr(ruletypes, rule)
        return True
    except AttributeError:
        return False


def get_subclasses(mod):
    """Yield the classes in module ``mod`` that inherit from ``cls``"""
    for name, obj in inspect.getmembers(mod):
        if hasattr(obj, "__bases__") and cls in obj.__bases__:
            for base in GENCLASSES:
                if base in obj.__bases__:
                    yield obj


def get_generators():
    """Find all rule generators in the rulegens package"""
    modules = pkgutil.iter_modules(path=["rulegens"])
    for loader, mod_name, ispkg in modules:
        mod = import_module('yaragen.rulegens.' + mod_name)
        for subcls in get_subclasses(mod_name, BaseGen):
            print subcls

class RuleGenManager():
    """The :py:class:`RuleGenManager` Manages and runs the rules
    to generate yara raules
    """

    def __init__(self, max_size,
                 min_size=10,
                 ratio=0.9,
                 fuzzy_len=6,
                 rulegen_list=None):
        """Constructor for the rule generator manager
        :param max_size: maximum rule size in bytes
        :type max_size: int
        :param min_size: minimum rule size in bytes
        :type min_size: int
        :param ratio: minimum ratio of matching bytes
        :type ratio: int
        :param fuzzy_len: max length of non matching bytes
        :type fuzzy_len: int
        :param rulegen_list: List of generators to use, all if None
        :type rulegen_list: List()
        """
        self.headergen_list = []
        valid_rulegens = get_generators()

        if rulegen_list is None:
            rulegen_list = valid_rulegens

        for rulegen in rulegen_list:
            if not rulegen in valid_rulegens:
                raise AttributeError("Invalid rulegenerator specified")
            if HeaderGen in rulegen.__mro__:
                self.headergen_list.append(rulegen())
            else:
                self.rulegen_list.append(rulegen(max_size, min_size,
                                                    ratio,
                                                    fuzzy_len))


    def compile_rules(rules):
        """Compile rules into yara format and return the buffer
        :param rules: list of yara rule types
        :type rules: List
        :rtype: rule buffer
        """
        rulebuff = ""
        for rule in rules:
            if is_ruletype(rule):
                pass
            else:
                raise AttributeError("Unable to compile, not valid rule type")

        return rulebuff

    def generate_starting_rules(self, buff1, buff2, blacklist_dict={}):
        """Generate rules using the provided buffers and chosen generators
        :param buff1: current buffer to generalise rules
        :type buff1: str
        :param buff2: current buffer to generalise rules
        :type buff2: str
        :param blacklist_dict: dictionary containing filename and buffers
        :type blacklist_dict: Dict()
        :rtype: list of rules"""
        rules = {}
        for gen in self.headergen_list:
            rules[gen], _ = gen.create_first_rules(buff1, buff2)
            # We should be checking to see whether we need to
            # run more header rules or not at this point and see
            # if the header can guide the other rules...

        for gen in self.rulegen_list:
            rules[gen] = gen.create_first_rules(buff1, buff2)

        # At this point we could run yara and cull rules from the blacklist,
        # it may make sense to do this later once we have fully specialised...
        return rules


    def generalise_rules(self, buff, rules, blacklist_dict={}):
        """Generate rules using the provided buffers and chosen generators
        :param buff: current buffer to generalise rules
        :type buff: str
        :param rules: list of currently generated rules
        :type list
        :param blacklist_dict: dictionary containing filename and buffers
        :type blacklist_dict: Dict()
        :rtype: list of rules"""

        # How are we going to manage the rules??
        for gen in self.headergen_list:
            rules[gen.__name__], _ = gen.generalise_rules(buff, rules)
            # We should be checking to see whether we need to
            # run more header rules or not at this point and see
            # if the header can guide the other rules

        for gen in self.rulegen_list:
            rules[gen.__name__] += gen.generalise_rules(buff, rules)

        # At this point we could run yara and cull rules from the blacklist,
        # it may make sense to do this later once we have fully specialised.

        return rules


    def generate_rules(self, buff_dict, blacklist={}):
        """Generate rules using the provided buffers and chosen generators
        :param buff_dict: dictionary containing filename and buffers
        :type buff_dict: Dict()
        :param blacklist_dict: dictionary containing filename and buffers
        :type blacklist_dict: Dict()
        :rtype: list of rules
        """
        rules = {}
        ordered = OrderedDict()
        # We want to order the buffers by size
        for k in sorted(buff_dict, key=lambda k: len(d[k]), reverse=True):
            ordered[k] = buff_dict[k]

        if len(ordered) < 2:
            raise ValueError("Must supply at least two buffers")

        comp_buff = ordered.popitem()

        while(comp_buff):
            if len(rules) == 0:
                gen_buff = comp_buff
                comp_buff = ordered.popitem()
                rules = self.generate_starting_rules(gen_buff,
                                                      comp_buff,
                                                      blacklist)
                continue

            rules = self.generalise_rules(comp_buff, rules, blacklist)
            comp_buff = ordered.popitem()

        return rules
