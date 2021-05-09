
__author__ = 'Daniel'


class Solution:
    def evaluateExpression(self, expression):
        
        post = self.infix2postfix(expression)
        return self.eval_postfix(post)

    def infix2postfix(self, lst):
        stk = []
        post = []  
        for elt in lst:
            if elt.isdigit():
                post.append(elt)
            else:
                if elt == "("":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""a""p""p""e""n""d""(""e""l""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""e""l""t"" ""=""="" 