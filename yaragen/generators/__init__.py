from abc import ABCMeta


class BaseGen():
    """The :py:class:`BaseGen` class is an abstract class defining the basic
        functionality required for a rule in yaragen
    
    """
    
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def create_first_rules(self, buff1, buff2):
        """Abstract method required to generate the initial rules used by
        yaragen
        
        :param buff1: The first buffer to compare
        :type buff1: str
        :param buff2: The second buffer to compare
        :type buff2: str
        :rtype: List of rules as expected in generalise_rules
        """
        return
        
        
    @abstractmethod
    def generalise_rules(self, buff, rules, blacklisted=False):
        """Abstract method required to generalize the current rules against
        a buffer
        
        :param buff: The buffer to compare gainst
        :type buff: str
        :param rules: List of rules to compare against buffer
        :type rules: List
        :param blacklisted: Is the current buffer in the blacklist
        :rtype: blacklisted: bool  
        """
        return


class HeaderGen(BaseGen):
    """The :py:class:`HeaderGen` class is an abstract class defining the basic
        functionality required for a header rule
        
        We 
    """

    __metaclass__ = ABCMeta

    @abstractmethod
    def create_first_rules(self, buff1, buff2):
        """Abstract method required to generate the initial rules used by
        yaragen
        
        :param buff1: The first buffer to compare
        :type buff1: str
        :param buff2: The second buffer to compare
        :type buff2: str
        :rtype: tuple, (list of rules, rangedict - {range, ruletypes})
        """
        return


    @abstractmethod
    def generalise_rules(self, buff, rules, blacklisted=False):
        """Abstract method required to generalize the current rules against
        a buffer
        
        :param buff: The buffer to compare against
        :type buff: str
        :param rules: List of rules to compare against buffer
        :type rules: List
        :param blacklisted: Is the current buffer in the blacklist
        :type blacklisted: bool
        :rtype: tuple, (list of rules, rangedict - {range, ruletypes})
        """
        return


class BinaryGen(BaseGen):
    """The :py:class:`BinaryGen` class is an abstract class defining the basic
        functionality required for a BinaryRule
        
        Binary rules should provide generation of rules based on binary data
    """

    __metaclass__ = ABCMeta

    def __init__(self, max_size, min_size=10, ratio=0.9, fuzzy_len=6):
        """Constructor for :py:class:`BinaryGen`
        
        :param max_size: maximum rule size in bytes
        :type max_size: int
        :param min_size: minimum rule size in bytes
        :type min_size: int
        :param ratio: minimum ratio of matching bytes
        :type ratio: int
        :param fuzzy_len: max length of non matching bytes
        :type fuzzy_len: int
        """
        self.max_size = max_size
        self.min_size = min_size
        self.ratio = ratio
        self.fuzzy_len = fuzzy_len


    @abstractmethod
    def create_first_rules(self, buff1, buff2):
        """Abstract method required to generate the initial rules used by
        yaragen
        
        :param buff1: The first buffer to compare
        :type buff1: str
        :param buff2: The second buffer to compare
        :type buff2: str
        :rtype: tuple, (list of rules, rangedict - {range, ruletypes})
        """
        return


    @abstractmethod
    def generalise_rules(self, buff, rules, blacklisted=False):
        """Abstract method required to generalize the current rules against
        a buffer
        
        :param buff: The buffer to compare against
        :type buff: str
        :param rules: List of rules to compare against buffer
        :type rules: List
        :param blacklisted: Is the current buffer in the blacklist
        :type blacklisted: bool  
        :rtype: tuple, (list of rules, rangedict - {range, ruletypes})
        """
        return

