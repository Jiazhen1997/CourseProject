
import math

__author__ = 'Danyang'


class Solution(object):
    def numTrees_math(self, n):
        
        return math.factorial(2*n)/(math.factorial(n)*math.factorial(n))-math.factorial(2*n)/(
            math.factorial(n+1)*math.factorial(n-1))

    def numTrees(self, n):
        
        if n < 2:
            return n

        dp = [0 for _ in xrange(n+1)]
        dp[0] = 1
        for i in xrange(1, n+1):
            for j in xrange(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""T""r""e""e""s""(""1""0""0"")"" ""=""="" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""T""r""e""e""s""_""m""a""t""h""(""1""0""0"")