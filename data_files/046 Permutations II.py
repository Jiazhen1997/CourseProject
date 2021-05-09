
__author__ = 'Danyang'
class Solution:
    def permuteUnique_TLE(self, num):
        
        result = []
        self.get_permute(num, [], result)
        return map(list, set(map(tuple, result)))


    def get_permute_TLE(self, nums, current, result):
        length = len(nums)
        if length==0:
            result.append(current)

        for ind, val in enumerate(nums):
            self.get_permute(nums[:ind]+nums[ind+1:], current+[val], result)


    def permuteUnique(self, num):
        
        result = []
        num.sort()
        self.get_permute(num, [], result)
        return result

    def get_permute(self, nums, current, result):
        if not nums:
            result.append(current)

        for ind, val in enumerate(nums):
            if ind-1>=0 and val==nums[ind-1]: continue  
            self.get_permute(nums[:ind]+nums[ind+1:], current+[val], result)

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""p""e""r""m""u""t""e""U""n""i""q""u""e""(""[""1"","" ""1"","" ""2""]"")