

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        mono = 0  
        for i in range(1, len(A)):
            if mono == 0:
                if A[i] > A[i-1]:
                    mono = 2
                elif A[i] < A[i-1]:
                    mono = 1
            else:
                if A[i] > A[i-1] and mono == 1:
                    return False
                elif A[i] < A[i-1] and mono == 2:
                    return False
        else:
            return True
