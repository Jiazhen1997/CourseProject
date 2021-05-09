
__author__ = 'Daniel'


class Solution(object):
    def integerBreak(self, n):
        
        F = [None for _ in xrange(n+1)]
        F[1] = 1
        for i in xrange(2, n+1):
            F[i] = max(
                max(F[j] * F[i-j], j * F[i-j], F[j] * (i-j), j * (i-j))
                for j in xrange(1, i/2)
            )

        return F[n]
