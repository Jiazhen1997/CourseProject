
__author__ = 'Danyang'


class Solution:
    def productExcludeItself(self, A):
        
        n = len(A)
        if n == 1:
            return []

        dp = [[1, 1] for _ in xrange(n)]
        for i in xrange(1, n):
            dp[i][0] = A[i-1]*dp[i-1][0]
            dp[n-i-1][1] = A[n-i]*dp[n-i][1]

        B = [dp[i][0]*dp[i][1] for i in xrange(n)]
        return B

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""r""o""d""u""c""t""E""x""c""l""u""d""e""I""t""s""e""l""f""(""[""1"","" ""2"","" ""3""]"")"" ""=""="" ""[""6"","" ""3"","" ""2""]