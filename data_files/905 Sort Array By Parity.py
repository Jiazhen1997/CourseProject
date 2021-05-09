

from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        closed = -1
        for i in range(len(A)):
            if A[i] % 2 == 0:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        return A
