



class Solution:
    def pivot(self, A, lo, hi):
        pivot = lo
        closed = pivot  
        for i in range(lo + 1, hi):
            if A[i] < A[pivot]:
                closed += 1
                A[closed], A[i] = A[i], A[closed]

        A[closed], A[pivot] = A[pivot], A[closed]
        return closed  

    def quick_select(self, nums, lo, hi, k):
        
        pivot = self.pivot(nums, lo, hi)
        if pivot == k:
            return nums[pivot]
        elif pivot > k:
            return self.quick_select(nums, lo, pivot, k)
        else:
            return self.quick_select(nums, pivot + 1, hi, k)


    def minMoves2(self, nums):
        
        n = len(nums)
        median = self.quick_select(nums, 0, n, n//2)
        return sum(map(lambda x: abs(x - median), nums))

    def find_median(self, nums):
        n = len(nums)
        nums.sort()
        return nums[n//2]

    def minMoves2_error(self, nums):
        
        n = len(nums)
        avg = round(sum(nums) / n)
        return sum(map(lambda x: abs(x - avg), nums))


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""M""o""v""e""s""2""(""[""1"",""2"",""3""]"")"" ""=""="" ""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""M""o""v""e""s""2""(""[""1"",""0"",""0"",""8"",""6""]"")"" ""=""="" ""1""4""
