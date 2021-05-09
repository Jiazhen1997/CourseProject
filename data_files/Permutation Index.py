
import math

__author__ = 'Daniel'


class Solution:
    def permutationIndex(self, A):
        
        n = len(A)
        idx = 0
        for i, v in enumerate(A):
            inv = 0
            for j in xrange(i+1, n):
                if A[i] > A[j]:
                    inv += 1

            idx += inv * math.factorial(n-1-i)

        return idx+1
