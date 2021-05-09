
__author__ = 'Danyang'


class Solution:
    def kthLargestElement(self, k, A):
        
        k = len(A)-k
        return self.find_kth(A, 0, len(A), k)

    def find_kth(self, A, i, j, k):
        p = self.pivot_optimized(A, i, j)
        if k == p:
            return A[p]
        elif k < p:
            return self.find_kth(A, i, p, k)
        else:
            return self.find_kth(A, p+1, j, k)

    def pivot(self, A, i, j):
        p = i
        closed = p
        for ptr in xrange(i, j):
            if A[ptr] < A[p]:
                closed += 1
                A[closed], A[ptr] = A[ptr], A[closed]

        A[closed], A[p] = A[p], A[closed]
        return closed

    def pivot_optimized(self, A, lo, hi):
        
        i = lo
        j = hi
        while True:
            while True:
                i += 1
                if i >= hi or A[i] >= A[lo]:
                    break
            while True:
                j -= 1
                if j < lo or A[j] <= A[lo]:
                    break

            if i >= j:
                break

            A[i], A[j] = A[j], A[i]

        A[lo], A[j] = A[j], A[lo]
        return j

    def pivot_3way(self, A, lo, hi):
        lt = lo-1  
        gt = hi  

        v = A[lo]
        i = lo  
        while i < gt:
            if A[i] < v:
                lt += 1
                A[lt], A[i] = A[i], A[lt]
                i += 1
            elif A[i] > v:
                gt -= 1
                A[gt], A[i] = A[i], A[gt]
            else:
                i += 1

        return lt+1, gt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""t""h""L""a""r""g""e""s""t""E""l""e""m""e""n""t""(""1""0"","" ""r""a""n""g""e""(""1"","" ""1""1"")"")"" ""=""="" ""1""
""
