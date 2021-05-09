
__author__ = 'Daniel'


class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        
        if not nums: return 0

        def msort(A, lo, hi):
            if hi - lo <= 1: return 0

            mid = (lo + hi)/2
            cnt = msort(A, lo, mid) + msort(A, mid, hi)

            temp = []
            i = j = r = mid
            for l in xrange(lo, mid):
                while i < hi and A[i] - A[l] <  lower: i += 1
                while j < hi and A[j] - A[l] <= upper: j += 1
                cnt += j - i

                while r < hi and A[r] < A[l]:
                    temp.append(A[r])
                    r += 1

                temp.append(A[l])

            while r < hi:  
                temp.append(A[r])
                r += 1

            A[lo:hi] = temp  
            return cnt

        n = len(nums)
        F = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            F[i] = F[i-1] + nums[i-1]

        return msort(F, 0, n+1)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""u""n""t""R""a""n""g""e""S""u""m""(""[""0"","" ""0""]"","" ""0"","" ""0"")"" ""=""="" ""3""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""u""n""t""R""a""n""g""e""S""u""m""(""[""-""2"","" ""5"","" ""-""1""]"","" ""-""2"","" ""2"")"" ""=""="" ""3""
