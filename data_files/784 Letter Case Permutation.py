

from typing import List


class Solution:
    def __init__(self):
        self.ret = []

    def letterCasePermutation(self, S: str) -> List[str]:
        
        
        S_lst = list(S)
        self.dfs([], S_lst, 0)
        return [
            "".""j""o""i""n""(""e"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""e"" ""i""n"" ""s""e""l""f"".""r""e""t""
"" "" "" "" "" "" "" "" ""]""
""
"" "" "" "" ""d""e""f"" ""d""f""s""(""s""e""l""f"","" ""l""s""t"","" ""S""_""l""s""t"","" ""i"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""l""e""n""(""l""s""t"")"" ""=""="" ""l""e""n""(""S""_""l""s""t"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""r""e""t"".""a""p""p""e""n""d""(""l""i""s""t""(""l""s""t"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" "" "" "" "" ""i""f"" ""S""_""l""s""t""[""i""]"".""i""s""d""i""g""i""t""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""a""p""p""e""n""d""(""S""_""l""s""t""[""i""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""l""s""t"","" ""S""_""l""s""t"","" ""i"" ""+"" ""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""p""o""p""("")""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""a""p""p""e""n""d""(""S""_""l""s""t""[""i""]"".""l""o""w""e""r""("")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""l""s""t"","" ""S""_""l""s""t"","" ""i"" ""+"" ""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""p""o""p""("")""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""a""p""p""e""n""d""(""S""_""l""s""t""[""i""]"".""u""p""p""e""r""("")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""l""s""t"","" ""S""_""l""s""t"","" ""i"" ""+"" ""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""s""t"".""p""o""p""("")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 