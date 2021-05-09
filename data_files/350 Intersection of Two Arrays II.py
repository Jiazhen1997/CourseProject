
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def intersect(self, nums1, nums2):
        
        h1, h2 = defaultdict(int), defaultdict(int)
        for a in nums1:
            h1[a] += 1
        for b in nums2:
            h2[b] += 1

        ret = []
        for k, v in h1.items():
            cnt = min(v, h2[k])
            ret.extend([k]*cnt)

        return ret


