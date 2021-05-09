
__author__ = 'Daniel'
from bisect import bisect_left, bisect_right


class Solution:
    def subarraySumII(self, A, start, end):
        
        n = len(A)
        cnt = 0
        f = [0 for _ in xrange(n+1)]

        for i in xrange(1, n+1):
            f[i] = f[i-1]+A[i-1]  

        f.sort()
        for i in xrange(n+1):
            lo = bisect_left(f, f[i]-end, 0, i)
            hi = bisect_right(f, f[i]-start, 0, i)
            cnt += hi-lo  

        return cnt

    def subarraySumII_TLE(self, A, start, end):
        
        n = len(A)
        cnt = 0
        f = [0 for _ in xrange(n+1)]

        for i in xrange(1, n+1):
            f[i] = f[i-1]+A[i-1]  

        for i in xrange(0, n+1):
            for j in xrange(i+1, n+1):
                s = f[j]-f[i]
                if start <= s <= end:
                    cnt += 1

        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""u""b""a""r""r""a""y""S""u""m""I""I""(""[""1"","" ""2"","" ""3"","" ""4""]"","" ""1"","" ""3"")"" ""=""="" ""4""
""
""
""
