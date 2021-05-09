
__author__ = 'Daniel'


class Solution:
    def summaryRanges(self, nums):
        
        ret = []
        n = len(nums)
        if n < 1:
            return ret

        bgn = nums[0]
        pre = nums[0]
        for i in xrange(1, n):
            if nums[i] != pre+1:
                if pre != bgn:
                    ret.append("%"d"-">"%"d""%""(""b""g""n"","" ""p""r""e"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"".""a""p""p""e""n""d""(