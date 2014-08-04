from rulegens import *
import ruletypes


def is_ruletype(rule):
    try:
        getattr(ruletypes, rule)
        return True
    except AttributeError:
        return False
    
    
def get_generators():
    return
