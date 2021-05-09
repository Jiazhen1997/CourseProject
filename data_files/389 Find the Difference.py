
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def findTheDifference(self, s, t):
        
        d = defaultdict(int)
        for e in s:
            d[e] += 1

        for e in t:
            if d[e] == 0:
                return e
            d[e] -= 1

        return 