
__author__ = 'Daniel'


class Solution:
    def calculate(self, s):
        
        lst = self.parse(s)
        post = self.infix2postfix(lst)
        return self.eval_postfix(post)

    def parse(self, s):
        
        i = 0
        ret = []
        while i < len(s):
            if s[i] == " "":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""s""[""i""]"" ""i""n"" ""(