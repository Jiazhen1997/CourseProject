

from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK_2(self, A: List[int], K: int) -> int:
        
        prefix_sum = 0
        counter = defaultdict(int)
        counter[0] = 1  
        for a in A:
            prefix_sum += a
            prefix_sum %= K
            counter[prefix_sum] += 1

        ret = 0
        for v in counter.values():
            ret += v * (v-1) // 2

        return ret

    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        prefix_sum = 0
        counter = defaultdict(int)
        counter[0] = 1  
        ret = 0
        for a in A:
            prefix_sum += a
            prefix_sum %= K
            ret += counter[prefix_sum]  
            counter[prefix_sum] += 1

        return ret
