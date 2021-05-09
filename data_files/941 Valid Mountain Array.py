

from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        incr = 0  
        for i in range(1, len(A)):
            if A[i] == A[i-1]:
                return False
            elif A[i] > A[i-1]:
                if incr == 2:
                    return False
                incr = 1
            else:
                if incr == 0:
                    return False
                incr = 2

        return incr == 2
