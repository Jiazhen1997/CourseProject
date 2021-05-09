
__author__ = 'Daniel'


class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        
        n = len(nums)
        ret = []
        if not nums:
            ret.append([lower, upper])
            return map(self.mapper, ret)

        if nums[0] > lower:
            ret.append([lower, nums[0]-1])

        for i in xrange(1, n):
            if nums[i] > nums[i-1]+1:
                ret.append([nums[i-1]+1, nums[i]-1])

        if upper > nums[-1]:
            ret.append([nums[-1]+1, upper])

        return map(self.mapper, ret)

    def mapper(self, x):
        if x[0] == x[1]:
            return "%"d"" ""%"" ""x""[""0""]""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 