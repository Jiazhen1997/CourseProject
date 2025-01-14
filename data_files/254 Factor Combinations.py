
from math import sqrt

__author__ = 'Daniel'


class Solution:
    def getFactors(self, n):
        
        ret = []
        self.dfs([n], ret)
        return ret

    def dfs(self, cur, ret):
        
        if len(cur) > 1:
            ret.append(list(cur))

        n = cur.pop()
        start = cur[-1] if cur else 2
        for i in xrange(start, int(sqrt(n))+1):
            if n % i == 0:
                cur.append(i)
                cur.append(n/i)
                self.dfs(cur, ret)
                cur.pop()

    def dfs2(self, n, cur, ret):
        if n > 1 and cur and len(cur) >= 1:
            ret.append(list(cur)+[n])

        start = cur[-1] if cur else 2
        for i in xrange(start, int(sqrt(n))+1):
            if n%i == 0:
                cur.append(i)
                self.dfs(n/i, cur, ret)
                cur.pop()

    def dfs_TLE(self, n, cur, ret):
        if n == 1 and cur and len(cur) >= 2:
            ret.append(list(cur))

        if cur:
            start = cur[-1]
        else:
            start = 2

        for i in xrange(start, int(sqrt(n+1))):
            if n%i == 0:
                cur.append(i)
                self.dfs_TLE(n/i, cur, ret)
                cur.pop()


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""g""e""t""F""a""c""t""o""r""s""(""1""6"")""
