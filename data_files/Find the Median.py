
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        if N % 2 == 1:
            return self.find_kth(A, 0, N - 1, (N - 1) / 2)
        else:
            raise IndexError

    def find_kth(self, A, i, j, k):
        
        p = self.partition(A, i, j)
        if p == k:
            return A[p]
        if p > k:
            return self.find_kth(A, i, p - 1, k)
        else:
            return self.find_kth(A, p + 1, j, k)

    def partition(self, A, i, j):
        if i > j:
            raise IndexError
        if i == j:
            return i

        p = i
        ptr_smaller = p
        for ptr in xrange(p + 1, j + 1):  
            if A[ptr] < A[p]:
                ptr_smaller += 1
                A[ptr], A[ptr_smaller] = A[ptr_smaller], A[ptr]

        A[p], A[ptr_smaller] = A[ptr_smaller], A[p]
        return ptr_smaller


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(