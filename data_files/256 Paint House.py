
import sys

__author__ = 'Daniel'


class Solution:
    
    
    def minCost(self, costs):
        
        if not costs:
            return 0

        n = len(costs)
        m = len(costs[0])
        F = [[0 for _ in xrange(m)] for _ in xrange(n+1)]
        for k in xrange(1, n+1):
            for i in xrange(m):
                F[k][i] = sys.maxint
                for j in xrange(m):
                    if i != j:
                        F[k][i] = min(F[k][i], F[k-1][j]+costs[k-1][i])

        return min(F[n][i] for i in xrange(m))


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""c""o""s""t""s"" ""="" ""[""[""7"","" ""6"","" ""2""]""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""C""o""s""t""(""c""o""s""t""s"")"" ""=""="" ""2