__author__ = 'Danyang'
class Solution:
    def solve(self, cipher, lst):
        
        N, K= cipher
        N = int(N)
        K = int(K)
        N = len(lst)
        dp = [[1<<32 for _ in xrange(N+1)] for _ in xrange(N+1)]
        for i in xrange(N):
            dp[i][i] = 1
            for j in xrange(i+1, N):
                dp[j][i] = 0
            dp[i][i+1] = 2

        for w in xrange(2, N+1):  
            for i in xrange(0, N-w):
                j = i+w
                if lst[j]-lst[i]==2*K:
                    for p in xrange(i+1, j):
                        if 2*lst[p]==lst[i]+lst[j] and dp[i+1][p-1]==0 and dp[p+1][j-1]==0:
                            dp[i][j] = 0

                if dp[i][j]!=0:
                    dp[i][j] = min(dp[i][j], min(dp[i][p]+dp[p+1][j] for p in xrange(i, j)))

        return dp[0][N-1]





if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(