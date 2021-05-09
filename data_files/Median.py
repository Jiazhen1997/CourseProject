
__author__ = 'Danyang'


class Solution:
    def median(self, nums):
        
        n = len(nums)
        return self.find_kth(nums, 0, n, (n-1)/2)

    def find_kth(self, A, i, j, k):
        p = self.pivot(A, i, j)
        if k == p:
            return A[p]
        elif k > p:
            return self.find_kth(A, p+1, j, k)
        else:
            return self.find_kth(A, i, p, k)

    def pivot(self, A, i, j):
        
        p = i
        closed = p
        for ptr in xrange(i, j):
            if A[ptr] < A[p]:
                closed += 1
                A[ptr], A[closed] = A[closed], A[ptr]

        A[closed], A[p] = A[p], A[closed]
        return closed


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""(""[""4"","" ""5"","" ""1"","" ""2"","" ""3""]"")"" ""=""="" ""3""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""(""[""7"","" ""9"","" ""4"","" ""5""]"")"" ""=""="" ""5""
