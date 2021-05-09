
__author__ = 'Daniel'


class Solution(object):
    def findMissing(self, nums):
        
        nth = -1
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == n:
                nth = nums[i]
                i += 1
            elif nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  
                
            else:
                i += 1

        if nth == -1:
            return n
        else:
            return nums.index(nth)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""i""s""s""i""n""g""(""[""9"",""8"",""7"",""6"",""2"",""0"",""1"",""5"",""4""]"")""
""
""
""
""
