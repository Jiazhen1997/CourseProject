

from typing import List


class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        
        F = 0
        ret = 0
        prev = -1
        for i, a in enumerate(A):
            if L <= a <= R:
                F = i - prev
                ret += F
            elif a > R:
                F = 0
                prev = i
            else:
                
                ret += F

        return ret

    def numSubarrayBoundedMax_error(self, A: List[int], L: int, R: int) -> int:
        
        F = 0
        ret = 0
        for a in A:
            if L <= a <= R:
                F += 1  
                ret += F
            elif a > R:
                F = 0
            else:
                
                ret += F

        return ret
