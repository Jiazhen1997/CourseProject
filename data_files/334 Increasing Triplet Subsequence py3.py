

from typing import List
from bisect import bisect_left


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        F = [float('inf') for _ in range(3)]
        for n in nums:
            i = bisect_left(F, n)
            if i >= 2:
                return True
            F[i] = n

        return False
