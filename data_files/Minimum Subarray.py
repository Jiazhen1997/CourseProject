
__author__ = 'Danyang'


class Solution:
    def minSubArray(self, nums):
        

        mini = min(nums)
        current = 0
        for a in nums:
            current += a
            mini = min(mini, current)
            if current > 0:
                current = 0

        return mini


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""S""u""b""A""r""r""a""y""(""[""1"","" ""-""1"","" ""-""2"","" ""1""]"")"" ""=""="" ""-""3""
""
""
