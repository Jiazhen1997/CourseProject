

import itertools
from typing import List
from collections import defaultdict


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        
        T = defaultdict(set)  
        for a, b, c in allowed:
            T[a, b].add(c)

        return self.dfs(T, bottom)

    def dfs(self, T, level) -> bool:
        if len(level) == 1:
            return True

        
        for nxt_level in itertools.product(
            *[T[a, b] for a, b in zip(level, level[1:])]
        ):
            if self.dfs(T, nxt_level):
                return True

        return False

    def gen_nxt_level(self, T, level, lo):
        
        if lo + 1 >= len(level):
            yield ""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""h""e""a""d"" ""i""n"" ""T""[""l""e""v""e""l""[""l""o""]"","" ""l""e""v""e""l""[""l""o"" ""+"" ""1""]""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""t""a""i""l"" ""i""n"" ""s""e""l""f"".""g""e""n""_""n""x""t""_""l""e""v""e""l""(""T"","" ""l""e""v""e""l"","" ""l""o"" ""+"" ""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""y""i""e""l""d"" ""h""e""a""d"" ""+"" ""t""a""i""l""
""
""
"" "" "" "" ""d""e""f"" ""d""f""s""_""d""e""e""p""(""s""e""l""f"","" ""T"","" ""l""e""v""e""l"","" ""l""o"","" ""n""x""t""_""l""e""v""e""l"")"" ""-"">"" ""b""o""o""l"":""
"" "" "" "" "" "" "" "" ""i""f"" ""l""o"" ""+"" ""1"" ""=""="" ""l""e""n""(""l""e""v""e""l"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""n""x""t"" ""i""n"" ""T""[""l""e""v""e""l""[""l""o""]"","" ""l""e""v""e""l""[""l""o"" ""+"" ""1""]""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""x""t""_""l""e""v""e""l"".""a""p""p""e""n""d""(""n""x""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""d""f""s""(""T"","" ""l""e""v""e""l"","" ""l""o"" ""+"" ""1"","" ""n""x""t""_""l""e""v""e""l"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""T""o""o"" ""d""e""e""p"" ""-"" ""c""h""e""c""k"" ""t""i""l""l"" ""t""o""p""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""d""f""s""(""T"","" ""n""x""t""_""l""e""v""e""l"","" ""0"","" ""[""]"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""x""t""_""l""e""v""e""l"".""p""o""p""("")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 