

from typing import List


class DisjointSet:
    def __init__(self):
        self.pi = {}

    def union(self, x, y):
        self.pi[self.find(x)] = self.find(y)

    def find(self, x):
        if x not in self.pi:
            self.pi[x] = x
        elif self.pi[x] != x:
            self.pi[x] = self.find(self.pi[x])
        return self.pi[x]

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        ds = DisjointSet()
        neqs = []  
        for e in equations:
            a = e[0]
            b = e[-1]
            sign = e[1:-1]
            if sign == "="="":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""d""s"".""u""n""i""o""n""(""a"","" ""b"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""n""e""q""s"".""a""p""p""e""n""d""(""(""a"","" ""b"")"")""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""a"","" ""b"" ""i""n"" ""n""e""q""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""d""s"".""f""i""n""d""(""a"")"" ""=""="" ""d""s"".""f""i""n""d""(""b"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
