
__author__ = 'Daniel'


class Solution(object):
    def maxProfit(self, A):
        
        n = len(A)
        if n == 0 or n == 1:
            return 0
        if n == 2:
            return max(0, A[1]-A[0])

        CD = 1  
        F = [0 for _ in xrange(n)]
        M = [0 for _ in xrange(n)]
        F[1] = A[1]-A[0]
        M[1] = max(M[0], F[1])
        F[2] = max(A[2]-A[2-1-i] for i in xrange(2))
        M[2] = max(M[1], F[2])

        
        for i in xrange(3, n):
            F[i] = max(F[i-1]+A[i]-A[i-1], M[i-2-CD]+A[i]-A[i-1])
            M[i] = max(M[i-1], F[i])

        return M[-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""f""i""t""(""[""1"","" ""2"","" ""3"","" ""0"","" ""2""]"")"" ""=""="" ""3