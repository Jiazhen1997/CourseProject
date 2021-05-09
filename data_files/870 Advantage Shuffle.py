

from typing import List
from collections import defaultdict


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        
        idxes = defaultdict(list)
        for i, b in enumerate(B):
            idxes[b].append(i)

        n = len(A)
        A.sort()
        B.sort()
        ret = [None for _ in range(n)]
        not_used = []
        j = 0
        for a in A:
            if a > B[j]:
                i = idxes[B[j]].pop()
                ret[i] = a
                j += 1
            else:
                not_used.append(a)

        for i in range(n):
            if ret[i] is None:
                ret[i] = not_used.pop()

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""a""d""v""a""n""t""a""g""e""C""o""u""n""t""(""[""2"",""7"",""1""1"",""1""5""]"","" ""[""1"",""1""0"",""4"",""1""1""]"")"" ""=""="" ""[""2"",""1""1"",""7"",""1""5""]""
