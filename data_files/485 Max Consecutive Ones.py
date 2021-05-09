



class Solution:
    def findMaxConsecutiveOnes(self, nums):
        
        s = 0
        e = 0
        ret = 0
        while s < len(nums):
            if nums[s] == 1:
                while e < len(nums) and nums[e] == 1:
                    e += 1
                ret = max(ret, e - s)
            else:
                e += 1

            s = e

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""a""x""C""o""n""s""e""c""u""t""i""v""e""O""n""e""s""(""[""1"",""1"",""0"",""1"",""1"",""1""]"")"" ""=""="" ""3""
