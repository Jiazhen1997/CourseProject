
__author__ = 'Danyang'


class Solution(object):
    def backPack(self, m, A):
        
        n = len(A)
        f = [0 for _ in xrange(m+1)]  
        for i in xrange(1, n+1):
            copy = list(f)
            for j in xrange(1, m+1):
                
                if j-A[i-1] >= 0:
                    f[j] = max(copy[j], copy[j-A[i-1]]+A[i-1])
                else:
                    f[j] = copy[j]
        return f[m]


class Solution_TLE(object):
    def backPack(self, m, A):
        
        result = [0]
        self.dfs(A, 0, m, result)
        return result[0]

    def dfs(self, seq, cur, m, result):
        if cur > m:
            return

        result[0] = max(result[0], cur)
        if seq:
            self.dfs(seq[1:], cur+seq[0], m, result)
            self.dfs(seq[1:], cur, m, result)


class Solution_MLE(object):
    def backPack(self, m, A):
        
        n = len(A)
        f = [[0 for _ in xrange(m+1)] for _ in xrange(n+1)]  
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                
                if j-A[i-1] >= 0:
                    f[i][j] = max(f[i-1][j], f[i-1][j-A[i-1]]+A[i-1])
                else:
                    f[i][j] = f[i-1][j]
        return f[n][m]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""b""a""c""k""P""a""c""k""(""1""1"","" ""[""2"","" ""3"","" ""5"","" ""7""]"")