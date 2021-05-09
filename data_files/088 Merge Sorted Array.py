
__author__ = 'Danyang'


class Solution(object):
    def merge(self, A, m, B, n):
        
        i = m-1
        j = n-1
        closed = m+n

        while i >= 0 and j >= 0:
            closed -= 1
            if A[i] > B[j]:
                A[closed] = A[i]
                i -= 1
            else:
                A[closed] = B[j]
                j -= 1

        
        
        if j >= 0: A[:closed] = B[:j+1]
        
