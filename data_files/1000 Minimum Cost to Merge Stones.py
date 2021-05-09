

from typing import List
from functools import lru_cache


class Solution:
    def mergeStones(self, stones: List[int], K: int) -> int:
        
        N = len(stones)
        sums = [0]
        for s in stones:
            sums.append(sums[-1] + s)

        @lru_cache(None)
        def F(i, j, m):
            if i >= j or m < 1:
                return float("i"n"f"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""n"" ""="" ""j"" ""-"" ""i""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""(""n"" ""-"" ""m"")"" ""%"" ""(""K"" ""-"" ""1"")"" ""!""="" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""f""l""o""a""t""(