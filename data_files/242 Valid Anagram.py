
from collections import defaultdict

__author__ = 'Daniel'


class Solution:
    def isAnagram(self, s, t):
        
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1

        for c in t:
            if c not in cnt or cnt[c] < 1:
                return False

            cnt[c] -= 1

        for v in cnt.values():
            if v != 0:
                return False

        return True
