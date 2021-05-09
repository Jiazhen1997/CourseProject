
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def longestPalindrome(self, s):
        
        c = defaultdict(int)
        for elt in s:
            c[elt] += 1

        ret = 0
        for v in c.values():
            ret += (v/2) * 2

        if any(map(lambda x: x % 2 == 1, c.values())):
            ret += 1

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""P""a""l""i""n""d""r""o""m""e""(