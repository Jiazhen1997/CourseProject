
__author__ = 'Daniel'


class Solution(object):
    def wiggleSort(self, A):
        
        n = len(A)
        median_idx = self.find_kth(A, 0, n, n/2)
        v = A[median_idx]

        idx = lambda i: (2*i+1) % (n|1)
        lt = -1
        hi = n
        i = 0
        while i < hi:
            if A[idx(i)] > v:
                lt += 1
                A[idx(lt)], A[idx(i)] = A[idx(i)], A[idx(lt)]
                i += 1
            elif A[idx(i)] == v:
                i += 1
            else:
                hi -= 1
                A[idx(hi)], A[idx(i)] = A[idx(i)], A[idx(hi)]

    def pivot(self, A, lo, hi, pidx=None):
        lt = lo-1
        gt = hi
        if not pidx: pidx = lo

        v = A[pidx]
        i = lo
        while i < gt:
            if A[i] < v:
                lt += 1
                A[lt], A[i] = A[i], A[lt]
                i += 1
            elif A[i] == v:
                i += 1
            else:
                gt -= 1
                A[gt], A[i] = A[i], A[gt]

        return lt, gt

    def find_kth(self, A, lo, hi, k):
        if lo >= hi: return

        lt, gt = self.pivot(A, lo, hi)

        if lt < k < gt:
            return k
        if k <= lt:
            return self.find_kth(A, lo, lt+1, k)
        else:
            return self.find_kth(A, gt, hi, k)


class SolutionSort(object):
    def wiggleSort(self, nums):
        
        n = len(nums)
        A = sorted(nums)

        j, k = (n-1) / 2, n-1
        for i in xrange(len(nums)):
            if i % 2 == 0:
                nums[i] = A[j]
                j -= 1
            else:
                nums[i] = A[k]
                k -= 1


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""#"" ""A"" ""="" ""[""1"","" ""5"","" ""1"","" ""1"","" ""6"","" ""4""]""
"" "" "" "" ""A"" ""="" ""[""3"","" ""2"","" ""1"","" ""1"","" ""3"","" ""2""]""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""w""i""g""g""l""e""S""o""r""t""(""A"")""
"" "" "" "" ""p""r""i""n""t"" ""A""
