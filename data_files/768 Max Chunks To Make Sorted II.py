

from typing import List
from collections import defaultdict, deque


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        A = sorted(arr)
        hm = defaultdict(deque)
        for i, e in enumerate(A):
            hm[e].append(i)

        proxy = []
        for e in arr:
            proxy.append(hm[e].popleft())

        ret = 0
        cur_max_idx = 0
        for i, e in enumerate(proxy):
            cur_max_idx = max(cur_max_idx, e)
            if cur_max_idx == i:
                ret += 1

        return ret
