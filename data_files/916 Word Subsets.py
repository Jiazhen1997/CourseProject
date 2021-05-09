

from typing import List
from collections import Counter, defaultdict


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        mx = defaultdict(int)
        for b in B:
            c = Counter(b)
            for k, v in c.items():
                mx[k] = max(mx[k], v)

        ret = []
        for a in A:
            c = Counter(a)
            for k, v in mx.items():
                if c[k] < v:
                    break
            else:
                ret.append(a)

        return ret
