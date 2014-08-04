from yaragen.rulegens import BinaryGen

class DiffBinaryGen(BinaryGen):
    """The :py:class:`DiffBinaryGen` Should use binary differencing
         to find appropriate hex based Yara rules
    """
    def create_first_rules(self, buff1, buff2):
        """Abstract method required to generate the initial rules used by
        yaragen
        
        :param buff1: The first buffer to compare
        :type buff1: str
        :param buff2: The second buffer to compare
        :type buff2: str
        :rtype: tuple, (list of rules)
        """
        return


    def generalise_rules(self, buff, rules, blacklisted=False):
        """Abstract method required to generalize the current rules against
        a buffer
        
        :param buff: The buffer to compare against
        :type buff: str
        :param rules: List of rules to compare against buffer
        :type rules: List
        :param blacklisted: Is the current buffer in the blacklist
        :type blacklisted: bool  
        :rtype: tuple, (list of rules)
        """
        return
