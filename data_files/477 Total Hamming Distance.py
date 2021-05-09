



class Solution:
    def totalHammingDistance(self, nums):
        
        ret = 0
        while any(nums):  
            z, o = 0, 0
            for i in range(len(nums)):
                if nums[i] & 1 == 0:
                    o += 1
                else:
                    z += 1
                nums[i] >>= 1

            ret += z * o

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""t""o""t""a""l""H""a""m""m""i""n""g""D""i""s""t""a""n""c""e""(""[""4"","" ""1""4"","" ""2""]"")"" ""=""="" ""6""
