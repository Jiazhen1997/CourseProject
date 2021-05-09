
from collections import defaultdict
import heapq

__author__ = 'Daniel'


class Counter(object):
    def __init__(self, val, cnt):
        self.val = val
        self.cnt = cnt

    def __cmp__(self, other):
        return self.cnt - other.cnt


class Solution(object):
    def topKFrequent(self, nums, K):
        
        cnt = defaultdict(int)
        for e in nums:
            cnt[e] += 1

        lst = []
        for k, v in cnt.items():
            lst.append(Counter(k, v))

        ret = []
        for elt in lst:
            if len(ret) < K:
                heapq.heappush(ret, elt)
            else:
                heapq.heappushpop(ret, elt)

        return map(lambda x: x.val, ret)

