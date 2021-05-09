

from bisect import bisect_left
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        char_pos = defaultdict(list)
        for p, c in enumerate(t):
            char_pos[c].append(p)
            

        lo_po = -1
        for c in s:
            if c not in char_pos:
                return False
            pos = char_pos[c]
            i = bisect_left(pos, lo_po)
            if i == len(pos):
                return False
            lo_po = pos[i] + 1  

        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""S""u""b""s""e""q""u""e""n""c""e""(