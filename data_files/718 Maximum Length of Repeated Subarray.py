

from typing import List
from collections import defaultdict


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        
        m, n = len(A), len(B)
        F = defaultdict(lambda: defaultdict(int))
        for i in range(1, m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    F[i][j] = F[i-1][j-1] + 1

        return max(
            F[i][j]
            for i in range(1, m+1)
            for j in range(1, n+1)
        )


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""L""e""n""g""t""h""(""[""1"",""2"",""3"",""2"",""1""]"","" ""[""3"",""2"",""1"",""4"",""7""]"")"" ""=""="" ""3""
