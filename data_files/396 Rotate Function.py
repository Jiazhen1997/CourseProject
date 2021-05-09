
import sys

__author__ = 'Daniel'


class Solution(object):
    def maxRotateFunction(self, A):
        
        if not A: return 0

        gmax = -sys.maxint
        n = len(A)
        s = sum(A)

        cur = sum(idx * val for idx, val in enumerate(A))
        for r in reversed(A):
            cur = cur + s - n * r
            gmax = max(gmax, cur)

        return gmax


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""R""o""t""a""t""e""F""u""n""c""t""i""o""n""(""[""4"","" ""3"","" ""2"","" ""6""]"")"" ""=""="" ""2""6""
