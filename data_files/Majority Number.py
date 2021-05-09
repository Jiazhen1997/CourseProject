
__author__ = 'Danyang'


class Solution:
    def majorityNumber(self, nums):
        
        cnt = 0
        maj = 0
        for ind, num in enumerate(nums):
            if num == nums[maj]:
                cnt += 1
            else:
                cnt -= 1  

            if cnt < 0:
                maj = ind
                cnt = 1

        
        return nums[maj]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""j""o""r""i""t""y""N""u""m""b""e""r""(""[""1"","" ""1"","" ""1"","" ""2"","" ""2"","" ""2"","" ""2"","" ""1"","" ""1""]"")"" ""=""="" ""1""
""
""
""
