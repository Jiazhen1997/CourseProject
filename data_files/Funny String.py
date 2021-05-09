

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        s = cipher
        r = s[::-1]
        s = map(ord, list(s))
        r = map(ord, list(r))
        for i in xrange(1, len(s)):
            if abs(s[i] - s[i - 1]) != abs(r[i] - r[i - 1]):
                return "N"o"t" "F"u"n"n"y""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 