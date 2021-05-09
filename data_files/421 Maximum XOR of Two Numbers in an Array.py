



class Solution:
    def findMaximumXOR(self, nums):
        
        ret = 0
        for i in reversed(range(32)):
            prefixes = set(num >> i for num in nums)
            ret <<= 1
            
            cur = ret + 1
            for p in prefixes:
                
                if cur ^ p in prefixes:
                    ret = cur
                    break  

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""a""x""i""m""u""m""X""O""R""(""[""3"","" ""1""0"","" ""5"","" ""2""5"","" ""2"","" ""8""]"")"" ""=""="" ""2""8""
