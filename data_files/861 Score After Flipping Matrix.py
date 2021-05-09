

from typing import List


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        
        m, n = len(A), len(A[0])
        ret = 0
        ret += (1 << (n-1)) * m  
        for j in range(1, n):
            cnt = 0
            for i in range(m):
                if A[i][j] == A[i][0]:
                    cnt += 1  

            
            cnt = max(cnt, m-cnt)
            ret += (1 << (n-1-j)) * cnt

        return ret
