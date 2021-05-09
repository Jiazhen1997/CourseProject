

from typing import List
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        F = defaultdict(lambda: defaultdict(lambda: 1))
        for i in range(len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                F[i][delta] = F[j][delta] + 1

        ret = 0
        for d in F.values():
            for v in d.values():
                ret = max(ret, v)

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""A""r""i""t""h""S""e""q""L""e""n""g""t""h""(""[""2""0"",""1"",""1""5"",""3"",""1""0"",""5"",""8""]"")"" ""=""="" ""4""
