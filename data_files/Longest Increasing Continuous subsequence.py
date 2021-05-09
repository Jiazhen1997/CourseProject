
__author__ = 'Daniel'


class Solution:
    def longestIncreasingContinuousSubsequence(self, A):
        
        n = len(A)
        if n < 1:
            return 0

        maxa = 1
        cur = 1
        for i in xrange(1, n):  
            if A[i] > A[i-1]:
                cur += 1
                maxa = max(maxa, cur)
            else:
                cur = 1

        cur = 1
        for i in xrange(1, n):  
            if A[n-1-i] > A[n-1-i+1]:
                cur += 1
                maxa = max(maxa, cur)
            else:
                cur = 1

        return maxa
