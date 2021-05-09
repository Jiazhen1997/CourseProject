

from typing import List
from collections import defaultdict


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        ret = 0
        for k, v in counter.items():
            if k + 1 in counter:
                ret = max(ret, v + counter[k + 1])

        return ret
