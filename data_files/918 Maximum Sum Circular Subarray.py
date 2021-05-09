

from typing import List


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        
        ret1 = self.max_subarray(A)
        ret2 = sum(A) + self.max_subarray([-a for a in A[1:-1]])  
        return max(ret1, ret2)

    def max_subarray(self, A) -> int:
        
        mx = -float('inf')
        cur = 0
        for a in A:
            cur = a + max(cur, 0)  
            mx = max(mx, cur)
        return mx

    def maxSubarraySumCircular_error(self, A: List[int]) -> int:
        
        cur = [0, None]
        mx = -float('inf')
        i = 0
        j = 0
        n = len(A)
        while i < n:
            cur[0] += A[i]
            cur[1] = i
            mx = max(mx, cur[0])
            j = i + 1
            while cur[0] >= 0 and j < i + n:
                cur[0] += A[j % n]
                mx = max(mx, cur[0])
                j += 1

            i = j

        return mx
