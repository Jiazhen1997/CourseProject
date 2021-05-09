

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        h = defaultdict(int)
        ret = 0
        s = 0
        h[s] += 1
        for n in nums:
            s += n
            ret += h[s - k]
            h[s] += 1

        return ret
