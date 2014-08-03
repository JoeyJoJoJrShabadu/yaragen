class YaraGenerator:
    """Yara interface"""
    
    def __init__(self):
        pass
        #Initialize yara c types here
        
    def gen_and_test_rule(self, rule, buffs):
        """Generate a yara rule and test it against a list of buffers
            rule: rule as a tuple of bytes, None used as wildcard
            buffs: list of buffers"""
        pass
    
    def gen_and_test_rules(self, rules, buffs):
        """Generate a yara rules and test it against a list of buffers
            rules: list of rules, a rule being a tuple of bytes, None used as wildcard
            buffs: list of buffers"""
        match = []
        for rule in rules:
            match.extend(self.gen_and_test_rule(rule, buffs))
        
        if len(match) == 0:
            return None
        
def create_yara_rule(self, rule):
    """Generates a yara rule from rule tuple
        rule: tuple of bytes, None used as wildcard
    """
    pass