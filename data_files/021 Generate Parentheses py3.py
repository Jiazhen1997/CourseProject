

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        F: List[List[str]] = [[] for _ in range(n + 1)]
        F[0].append("")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""1"","" ""n""+""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""r""a""n""g""e""(""i"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""s""1"" ""i""n"" ""F""[""j""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""s""2"" ""i""n"" ""F""[""i""-""j""-""1""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""F""[""i""]"".""a""p""p""e""n""d""(""f