

from typing import List


class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        
        m, n = len(A), len(A[0])
        lt = [False for i in range(m)]
        deleted = 0
        for j in range(n):
            for i in range(m-1):
                if lt[i]:
                    continue
                if A[i][j] > A[i+1][j]:
                    deleted += 1
                    break
            else:  
                
                for i in range(m-1):
                    lt[i] = lt[i] or A[i][j] < A[i+1][j]

        return deleted
