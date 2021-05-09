

__author__ = 'Daniel'


class Solution(object):
    def moveZeroes(self, nums):
        
        left = -1
        for i in xrange(len(nums)):
            if nums[i] != 0:
                left += 1
                nums[left], nums[i] = nums[i], nums[left]


class SolutionCount(object):
    def moveZeroes(self, nums):
        
        cnt = 0
        for elt in nums:
            if elt != 0:
                nums[cnt] = elt
                cnt += 1

        for j in xrange(cnt, len(nums)):
            nums[j] = 0


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""s""t"" ""="" ""[""0"","" ""1"","" ""0"","" ""3"","" ""1""2""]""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""m""o""v""e""Z""e""r""o""e""s""(""l""s""t"")""
"" "" "" "" ""a""s""s""e""r""t"" ""l""s""t"" ""=""="" ""[""1"","" ""3"","" ""1""2"","" ""0"","" ""0""]""
