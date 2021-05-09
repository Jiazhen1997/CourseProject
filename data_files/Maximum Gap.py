

__author__ = 'Daniel'
import sys


class Solution:
    def maximumGap(self, nums):
        
        n = len(nums)
        if n < 2:
            return 0

        gmax = max(nums)
        gmin = min(nums)
        bin_width = max(1, (gmax-gmin)/(n-1))  

        bins_max = {}  
        bins_min = {}

        for elt in nums:
            bin_num = (elt-gmin)/bin_width
            bins_min[bin_num] = min(bins_min.get(bin_num, sys.maxint), elt)
            bins_max[bin_num] = max(bins_max.get(bin_num, -sys.maxint-1), elt)

        max_gap = -1
        pre_bin_max = gmin
        for i in xrange((gmax-gmin)/bin_width+1):
            if i in bins_min:
                max_gap = max(max_gap, bins_min[i]-pre_bin_max)
                pre_bin_max = bins_max[i]

        return max_gap

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""i""m""u""m""G""a""p""(""[""1"","" ""9"","" ""2"","" ""5""]"")"" ""=""="" ""4