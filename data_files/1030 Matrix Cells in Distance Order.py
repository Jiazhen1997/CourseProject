

from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        
        r_max = max(r0, R-1 - r0)
        c_max = max(c0, C-1 - c0)
        lst = [[] for _ in range(r_max + c_max + 1)]
        for i in range(R):
            for j in range(C):
                lst[abs(i - r0) + abs(j - c0)].append([i, j])

        ret = []
        for e in lst:
            ret.extend(e)

        return ret
