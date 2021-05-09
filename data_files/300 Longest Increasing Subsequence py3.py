

from typing import List
from bisect import bisect_left


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        F = [float('inf') for _ in nums]
        l = 0
        for n in nums:
            i = bisect_left(F, n)  
            F[i] = n
            l = max(l, i + 1)

        return l
