"""
Only leaving this here for some base code for James to get started on
even though I think using this as a base is a terrible idea....
"""

class RuleGenerator:
    """Compare binaries to generate rules
        p_buffs: list of buffers to match
        n_buffs: list of buffers not to match"""
    
    def __init__(self, p_buffs, n_buffs):
        self.p_buffs = p_buffs
        self.n_buffs = n_buffs
        self.compare = Compare(0.75)
        
        
    def tune_rules(self, ruleset, buff, min_size, ratio):
        """Tune rules to the buffer, culling the rules if a match cannot be
        made at the given ratio
            ruleset: list of rules
            buffer: buffer to test rules against
            min_size: minimum size of possible match
            ratio: minimum match ratio"""
        #need to order rules by length = or do I?
        new_ruleset = []
        
        for rule in ruleset:
            window_size = rule.length()
            match = None
            i = 0
            while (match is None) and (i <= len(buffer) - window_size):
                match = self.compare.tune_rule_start(rule, buff[i:i+window_size])
                i += 1 
            if match:
                new_ruleset.append(match)
        
        return new_ruleset
        
    def get_starting_rules(self, first, second, min_size, ratio):
        """Generate starting rules by comparing two of the buffers and then
        checking for subsets of rules
            first: first buffer
            second: second buffer
            min_size: minimum match byte length
            ratio: minimum match ratio"""
        start_rules = []
        found_range = []
        size = len(first)
        #Generate rules by comparing two buffers
        while size > min_size:
            for i in range(0, len(first)):
                if i in found_range:
                    i += 1
                    continue
                if i + size > len(first):
                    break
                for j in range(0, len(second)):
                    match = self.compare.tune_rule_within(first[i:i+size], second[j:])
                    if match:
                        start_rules.append(match)
                        found_range.extend(range(i, i + len(match)))
                        i += len(match)
                        j += len(match)
                    j += 1
                i += 1
            size -= 1
        
        #order rules by length
        #Gotta be a better way to do thiS!!!
        superset_rules = set()
        for rule1 in start_rules:
            for rule2 in start_rules:
                if rule1 != rule2 and len(rule1) < len(rule2):
                    match = self.compare.tune_rule_within(start_rules[i], start_rules[j], ratio = 1)
                    superset_rules.add(match)
        
        return superset_rules
    
    def remove_neg_rules(self, rules, buffs):
        """Generate Yara rules then run them against a list of buffers
            rules: byte tuple, None as wildcard
            buffs: list of buffers"""
        self.yaragen = YaraGenerator()
        matched_rules = self.yaragen.gen_and_test_rules(rules, self.n_buffs)
        for rule in matched_rules:
            rules.remove(rule)
            
        return matched_rules
                
    def get_rules(self, min_size=4, ratio=0.75):
        """get a set of rules that match the buffer constraints and have a length
        larger than 4 and a ratio of matched bytes, to not match above ratio
            min_size: the minimum length of match required
            ratio: the ratio required"""
        #sor by length
        first = self.p_buffs[0]
        second = self.p_buffs[1]
        
        ruleset = self.get_starting_rules(first, second, min_size, ratio)
        ruleset = self.remove_neg_rules(ruleset, self.n_buffs)
        
