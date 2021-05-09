

from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        
        cur = 0
        ret = []
        for a in A:
            cur = (cur << 1) + a
            cur %= 5
            if cur == 0:
                ret.append(True)
            else:
                ret.append(False)

        return ret
