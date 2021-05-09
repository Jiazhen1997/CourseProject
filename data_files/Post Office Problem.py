
__author__ = 'Daniel'


class Solution:
    def postOffice_TLE(self, A, K):
        
        A.sort()
        N = len(A)
        F = [[0 for _ in xrange(K+1)] for _ in xrange(N+1)]
        c = [[0 for _ in xrange(N+1)] for _ in xrange(N+1)]  

        for i in xrange(N):
            for j in xrange(i+1, N+1):
                m = (i+j)/2
                for l in xrange(i, j):
                    c[i][j] += abs(A[m]-A[l])

        for n in xrange(1, N+1):
            F[n][1] = c[0][n]

        for n in xrange(1, N+1):
            for k in xrange(2, K+1):
                F[n][k] = min(
                    F[l][k-1]+c[l][n] for l in xrange(n)
                )

        return F[N][K]

    def postOffice_TLE(self, A, K):
        
        


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""o""s""t""O""f""f""i""c""e""(""[""1""1""2"",""1""2""2"",""3""6""0"",""3""1""1"",""8""5"",""2""2""5"",""4""0""5"",""5""3"",""4""0""5"",""4""3"",""3""4""2"",""1""3"",""5""8""8"",""4""2""4"",""2""9""9"",""3""7"",""1""0""4"",""2""8""9"",""4""0""4"",""4""1""4""]"","" ""3"")"" ""=""="" ""6""7""3