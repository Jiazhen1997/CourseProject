
import sys

__author__ = 'Daniel'


class Solution(object):
    def minCostII(self, costs):
        
        if not costs:
            return 0

        n = len(costs)
        m = len(costs[0])
        F = [[0 for _ in xrange(m)] for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            for k1 in xrange(m):
                F[i][k1] = min(
                    F[i-1][k0]+costs[i-1][k1]
                    
                    for k0 in xrange(m)
                    if i == 1 or k1 != k0
                )

        return min(F[n][i] for i in xrange(m))


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""C""o""s""t""I""I""(""[""[""8""]""]"")"" ""=""="" ""8