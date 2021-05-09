
from math import sqrt, floor, ceil

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        l = len(cipher)
        r = range(int(floor(sqrt(l))), int(ceil(sqrt(l))) + 1)

        min_pair = (r[-1], r[-1])
        for h in r:
            for w in r:
                if h * w >= l and h * w < min_pair[0] * min_pair[1]:
                    min_pair = (h, w)
        h, w = min_pair
        rect = [[None for _ in xrange(w)] for _ in xrange(h)]
        for i in xrange(l):
            rect[i / w][i % w] = cipher[i]

        result = []
        for j in xrange(w):
            sb = []
            for i in xrange(h):
                if rect[i][j] == None: break
                sb.append(rect[i][j])
            result.append("".""j""o""i""n""(""s""b"")"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 