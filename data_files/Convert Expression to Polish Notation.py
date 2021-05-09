
__author__ = 'Daniel'


class Solution:
    def convertToPN(self, expression):
        
        return self.infix2prefix(expression)

    def infix2prefix(self, lst):
        
        stk = []
        pre = []
        for elt in reversed(lst):
            if elt.isdigit():
                pre.append(elt)
            elif elt == ")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""a""p""p""e""n""d""(""e""l""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""e""l""t"" ""=""="" 