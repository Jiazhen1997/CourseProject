
__author__ = 'Daniel'


class Solution(object):
    def canWinNim(self, n):
        
        return n % 4 != 0

    def canWinNim_TLE(self, n):
        
        if n < 3:
            return True

        F = [False for _ in xrange(3)]
        F[1] = F[2] = F[0] = True
        for i in xrange(4, n+1):
            F[i%3] = any(not F[(i-k)%3] for k in xrange(1, 4))

        return F[n%3]

    def canWinNim_MLE(self, n):
        
        if n < 3:
            return True

        F = [False for _ in xrange(n+1)]
        F[1] = F[2] = F[3] = True
        for i in xrange(4, n+1):
            F[i] = any(not F[i-k] for k in xrange(1, 4))

        return F[n]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""W""i""n""N""i""m""(""5"")