

from typing import List
from collections import deque


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        n = len(A)
        ret = deque()
        lo = 0
        hi = n
        while lo < hi:
            if A[lo] ** 2 < A[hi - 1] ** 2:
                ret.appendleft(A[hi - 1] ** 2)
                hi -= 1
            else:
                ret.appendleft(A[lo] ** 2)
                lo += 1

        return list(ret)
