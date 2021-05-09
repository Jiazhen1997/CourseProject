
__author__ = 'Daniel'


class Solution:
    def evalRPN(self, tokens):
        
        return self.eval_postfix(tokens)

    def eval_postfix(self, post):
        stk = []
        for elt in post:
            if elt.strip("-"")"".""i""s""d""i""g""i""t""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""a""p""p""e""n""d""(""i""n""t""(""e""l""t"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""b"" ""="" ""s""t""k"".""p""o""p""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""a"" ""="" ""s""t""k"".""p""o""p""("")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""e""l""t"" ""=""="" 