



class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        return self.make_stk(S) == self.make_stk(T)

    def make_stk(self, S):
        stk = []
        for s in S:
            if s == "#"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""t""k"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""p""o""p""("")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""a""p""p""e""n""d""(""s"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""t""k""
