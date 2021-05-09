
__author__ = 'Danyang'


class Solution:
    def longestCommonSubstring(self, A, B):
        
        m = len(A)
        n = len(B)
        f = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]

        if m == 0 or n == 0:
            return 0

        maxa = -1
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1]+1
                else:
                    f[i][j] = 0
                maxa = max(maxa, f[i][j])

        return maxa  
