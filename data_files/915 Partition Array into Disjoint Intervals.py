

from typing import List


class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        
        n = len(A)
        MX = [-float('inf') for _ in range(n+1)]
        MI = [float('inf') for _ in range(n+1)]
        for i in range(n):
            MX[i+1] = max(M[i], A[i])
        for i in range(n-1, -1, -1):
            MI[i] = min(MI[i+1], A[i])

        for l in range(1, n+1):
            if MX[l] <= MI[l]:
                return l
        raise

    def partitionDisjoint_2(self, A: List[int]) -> int:
        
        MX = [0 for _ in A]
        MI = [0 for _ in A]
        MX[0] = A[0]
        MI[-1] = A[-1]
        n = len(A)
        for i in range(1, n):
            MX[i] = max(MX[i-1], A[i])
        for i in range(n-2, -1, -1):
            MI[i] = min(MI[i+1], A[i])

        for i in range(n-1):
            if MX[i] <= MI[i+1]:
                return i

        raise
