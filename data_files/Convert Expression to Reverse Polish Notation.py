
__author__ = 'Daniel'


class Solution(object):
    def convertToRPN(self, expression):
        
        return self.infix2postfix(expression)

    def infix2postfix(self, lst):
        
        stk = []
        ret = []  
        for elt in lst:
            if elt.isdigit():
                ret.append(elt)
            elif elt == "("":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""a""p""p""e""n""d""(""e""l""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""e""l""t"" ""=""="" 