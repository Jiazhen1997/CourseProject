
__author__ = 'Daniel'


class Solution(object):
    def wiggleMaxLength(self, A):
        
        if not A: return 0
        N = len(A)
        H = [1 for _ in xrange(N)]
        L = [1 for _ in xrange(N)]
        for i in xrange(1, N):
            L[i] = H[i-1] + 1 if A[i] < A[i-1] else L[i-1]
            H[i] = L[i-1] + 1 if A[i] > A[i-1] else H[i-1]

        return max(H[N-1], L[N-1])

    def wiggleMaxLengthSuboptimal(self, A):
        
        if not A: return 0

        N = len(A)
        H = [1 for _ in xrange(N)]
        L = [1 for _ in xrange(N)]
        gmax = 1
        for i in xrange(1, N):
            for j in xrange(i):
                if A[i] > A[j]:
                    H[i] = max(H[i], L[j] + 1)
                elif A[i] < A[j]:
                    L[i] = max(L[i], H[j] + 1)

                gmax = max(gmax, H[i], L[i])

        return gmax
