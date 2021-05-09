

from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        lasts = {}
        n = len(S)
        for i in range(n-1, -1, -1):
            if S[i] not in lasts:
                lasts[S[i]] = i

        indexes = [-1]  
        cur_last = 0
        for i in range(n):
            cur_last = max(cur_last, lasts[S[i]])
            if cur_last == i:
                indexes.append(cur_last)

        ret = []
        for i in range(len(indexes) - 1):
            ret.append(indexes[i+1] - indexes[i])
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""a""r""t""i""t""i""o""n""L""a""b""e""l""s""(