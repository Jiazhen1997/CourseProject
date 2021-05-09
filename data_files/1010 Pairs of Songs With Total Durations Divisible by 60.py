

from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        
        counter = defaultdict(int)
        ret = 0
        for t in time:
            ret += counter[(60 - t) % 60]  
            counter[t % 60] += 1

        return ret


    def numPairsDivisibleBy60_error(self, time: List[int]) -> int:
        
        hm = defaultdict(int)
        for t in time:
            hm[t % 60] += 1

        ret = 0
        for k, v in hm.items():
            if k == 0:
                ret += (v * (v - 1)) // 2
            elif k <= 60 - k:  
                v2 =  hm[60 - k]
                ret += v2 * v

        return ret
