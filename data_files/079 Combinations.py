
__author__ = 'Danyang'
class Solution:
    def combine(self, n, k):
        
        result = []
        nums = [i+1 for i in xrange(n)]  
        self.get_combination(k, nums, [], result)
        return result

    def get_combination(self, k, nums, current, result):
        if len(current)==k:
            result.append(current)
            return  
        elif len(current)+len(nums)<k:
            return  

        for ind, val in enumerate(nums):
            
            self.get_combination(k, nums[ind+1:], current+[val], result)  
            
            
            


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""m""b""i""n""e""(""4"","" ""2"")