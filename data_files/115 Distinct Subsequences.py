
__author__ = 'Danyang'
class Solution:
    def numDistinct(self, S, T):
        
        len_s = len(S)
        len_t = len(T)

        dp = [[-1 for _ in xrange(len_s+1)] for _ in xrange(len_t+1)]
        for col in xrange(len_s+1):
            dp[0][col] = 1
        for row in xrange(1, len_t+1):
            dp[row][0] = 0

        for row in xrange(1, len_t+1):
            for col in xrange(1, len_s+1):
                if S[col-1]==T[row-1]:
                    dp[row][col] = dp[row][col-1]+dp[row-1][col-1]
                else:
                    dp[row][col] = dp[row][col-1]

        return dp[-1][-1]

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""D""i""s""t""i""n""c""t""(