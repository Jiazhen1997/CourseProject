
__author__ = 'Daniel'
import heapq
from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums, k):
        
        d = defaultdict(list)
        for i, v in enumerate(nums):
            heapq.heappush(d[v], i)

        for v in d.values():
            if len(v) > 1:
                pre = heapq.heappop(v)
                while v:
                    cur = heapq.heappop(v)
                    if cur-pre <= k:
                        return True
                    pre = cur

        return False