
__author__ = 'Daniel'


class Solution(object):
    def getMoneyAmount(self, n):
        
        N = n + 1  
        F = [[0 for _ in xrange(N+1)] for _ in xrange(N+1)]
        for i in xrange(n, 0, -1):
            for j in xrange(i+2, N+1):
                F[i][j] = min(
                    k + max(F[i][k], F[k+1][j])
                    for k in xrange(i, j)
                )

        return F[1][N]

    def getMoneyAmountError(self, n):
        
        C = [0 for _ in xrange(n+1)]
        F = [0 for _ in xrange(n+1)]
        for i in xrange(2, n+1):
            C[i] = min(1 + max(C[k-1], C[i-k]) for k in xrange(1, i+1))
            F[i] = min(k + max(F[k-1], k*C[i-k] + F[i-k]) for k in xrange(1, i+1))

        return F[n]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""g""e""t""M""o""n""e""y""A""m""o""u""n""t""(""1""0""0"")""
""
