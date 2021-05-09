
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def longestSubstring(self, s, k):
        
        if not s:
            return 0

        cnt = defaultdict(int)
        for e in s: cnt[e] += 1

        c = min(
            s,
            key=lambda x: cnt[x],
        )

        if cnt[c] >= k:
            return len(s)

        return max(
            map(lambda x: self.longestSubstring(x, k), s.split(c))
        )
