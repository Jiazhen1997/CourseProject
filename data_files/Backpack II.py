
__author__ = 'Danyang'


class Solution:
    def backPackII(self, m, A, V):
        
        n = len(A)
        f = [0 for _ in xrange(m+1)]  
        for i in xrange(1, n+1):
            copy = list(f)
            for j in xrange(1, m+1):
                
                if j-A[i-1]>=0:
                    f[j] = max(copy[j], copy[j-A[i-1]]+V[i-1])
                else:
                    f[j] = copy[j]
        return f[m]