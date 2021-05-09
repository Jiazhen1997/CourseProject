
__author__ = 'Daniel'


class Solution:
    def maxSquare(self, matrix):
        
        M = len(matrix)
        N = len(matrix[0])
        F = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]

        gmax = 0
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if matrix[i-1][j-1] == 1:
                    F[i][j] = min(F[i-1][j], F[i][j-1], F[i-1][j-1])+1
                    gmax = max(gmax, F[i][j])

        return gmax*gmax

    def maxSquare_error(self, matrix):
        
        M = len(matrix)
        N = len(matrix[0])
        h = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if matrix[i-1][j-1] == 1:
                    h[i][j] = h[i-1][j]+1
                else:
                    h[i][j] = 0

        ret = 0
        for i in xrange(M):
            stk = []  
            for j in xrange(N):
                while stk and h[i+1][stk[-1]+1] >= h[i+1][j+1]:
                    stk.pop()
                idx = -1
                if stk: idx = stk[-1]
                cur_square = min(j-idx, h[i+1][j+1])
                cur_square *= cur_square
                ret = max(ret, cur_square)
                stk.append(j)

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""S""q""u""a""r""e""(""[""[""0"",""1"",""0"",""1"",""1"",""0""]"",""[""1"",""0"",""1"",""0"",""1"",""1""]"",""[""1"",""1"",""1"",""1"",""1"",""0""]"",""[""1"",""1"",""1"",""1"",""1"",""1""]"",""[""0"",""0"",""1"",""1"",""1"",""0""]"",""[""1"",""1"",""1"",""0"",""1"",""1""]""]""
"" "" "" "" "")"" ""=""="" ""9