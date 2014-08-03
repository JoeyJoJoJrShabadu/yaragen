import difflib

class Compare:
    """ The compare class provides binary comparison functions using difflib"""
    
    def __init__(self, ratio):
        self.ration = ratio
        
    def tune_rule_start(self, rule, buffer, ratio=None):
        """Try match rule only from start of buffer, generate closest 
        possible match at ratio or return none
            rule: rule to tune
            buffer: buffer to tune against
            ratio: ratio of matching bytes"""
        if not ratio:
            self.ratio = ratio
    
    def tune_rule_within(self, rule, buffer, ratio=None):
        """Try match rule anywhere within buffer, generate closest
        possible match > ratio or return None
            rule: rule to tune
            buffer: buffer to tune against
            ratio: ratio of matching bytes"""
        if not ratio:
            self.ratio = ratio