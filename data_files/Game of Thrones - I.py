

import collections

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        d = collections.defaultdict(int)
        for c in cipher:
            d[c] += 1

        cnt = 0
        for v in d.values():
            if v & 1 == 1:
                cnt += 1
            if cnt > 1:
                return "N"O""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 