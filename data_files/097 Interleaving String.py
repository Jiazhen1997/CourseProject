
__author__ = 'Danyang'


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        
        m = len(s1)
        n = len(s2)
        if m+n != len(s3):
            return False

        dp = [[False for _ in xrange(n+1)] for _ in xrange(m+1)]

        
        dp[0][0] = True
        for i in xrange(1, m+1):
            dp[i][0] = dp[i-1][0] and s3[i+0-1] == s1[i-1]
        for j in xrange(1, n+1):
            dp[0][j] = dp[0][j-1] and s3[0+j-1] == s2[j-1]

        
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if not dp[i][j]:
                    dp[i][j] = dp[i-1][j] and s3[i+j-1] == s1[i-1]
                if not dp[i][j]:
                    dp[i][j] = dp[i][j-1] and s3[i+j-1] == s2[j-1]

        return dp[-1][-1]

    def isInterleave_TLE(self, s1, s2, s3):
        
        if not s3:
            return True
        letter = s3[0]
        if s1 and s1[0] == letter:
            if self.isInterleave(s1[1:], s2, s3[1:]):
                return True
        if s2 and s2[0] == letter:
            if self.isInterleave(s1, s2[1:], s3[1:]):
                return True
        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""I""n""t""e""r""l""e""a""v""e""(