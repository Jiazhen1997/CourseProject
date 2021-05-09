

from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        
        return max(0, max(A) - K - (min(A) + K))
