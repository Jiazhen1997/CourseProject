
__author__ = 'Daniel'


class Solution(object):
    def maxSubArrayLen(self, A, k):
        
        m = {0: -1}  
        maxa = 0
        s = 0
        for i in xrange(len(A)):
            s += A[i]
            t = s - k  
            if t in m:
                maxa = max(maxa, i - m[t])

            if s not in m:
                m[s] = i

        return maxa
