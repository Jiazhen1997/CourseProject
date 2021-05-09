
__author__ = 'Daniel'


class Solution(object):
    def missingNumber(self, nums):
        
        num_n = None
        n = len(nums)

        i = 0
        while i < n:
            if nums[i] == n:
                num_n = nums[i]
                nums[i] = None
                i += 1

            elif nums[i] is not None and nums[i] != i:
                j = nums[i]
                nums[i], nums[j] = nums[j], nums[i]

            else:
                i += 1

        if not num_n:
            return n

        return nums.index(None)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""s""s""i""n""g""N""u""m""b""e""r""(""[""2"","" ""0""]"")"" ""=""="" ""1""
