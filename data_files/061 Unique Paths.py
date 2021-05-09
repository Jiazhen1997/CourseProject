
import math
__author__ = 'Danyang'


class Solution(object):
    def uniquePaths(self, m, n):
        
        m -= 1
        n -= 1
        return math.factorial(m+n) / (math.factorial(n) * math.factorial(m))

    def uniquePathsDP(self, m, n):
        F = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        F[1][0] = 1  
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                F[i][j] = F[i-1][j] + F[i][j-1]

        return F[m][n]

    def uniquePathsNormal(self, m, n):
        
        F = [[0 for _ in xrange(n)] for _ in xrange(m)]
        F[0][0] = 1  

        
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0: continue
                if i == 0: F[i][j] = F[i][j-1]
                elif j == 0: F[i][j] = F[i-1][j]
                else: F[i][j] = F[i-1][j]+F[i][j-1]

        return F[m-1][n-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""u""n""i""q""u""e""P""a""t""h""s""(""3"","" ""7"")"" ""=""="" ""2""8