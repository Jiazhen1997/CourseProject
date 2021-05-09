



class Solution:
    def checkSubarraySum(self, nums, k):
        
        h = {0: 0}  
        s = 0
        for l in range(1, len(nums) + 1):
            s += nums[l-1]
            if k != 0:  
                s %= k
            if s in h:
                if l - h[s] >= 2:  
                    return True
            else:
                
                h[s] = l

        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""h""e""c""k""S""u""b""a""r""r""a""y""S""u""m""(""[""2""3"",""2"",""4"",""6"",""7""]"","" ""6"")"" ""=""="" ""T""r""u""e""
