
__author__ = 'Daniel'
import sys


class Solution:
    def maximumGap(self, nums):
        
        n = len(nums)
        if n < 2:
            return 0

        g_min = min(nums)
        g_max = max(nums)

        bin_width = max(1, (g_max-g_min)/n)
        bins_min = {}
        bins_max = {}
        for v in nums:
            bin_id = (v-g_min)/bin_width
            bins_min[bin_id] = min(bins_min.get(bin_id, sys.maxint), v)
            bins_max[bin_id] = max(bins_max.get(bin_id, -sys.maxint-1), v)

        max_gap = 0
        pre_max = g_min
        for i in xrange(0, (g_max-g_min)/bin_width+1):
            if i in bins_min:
                max_gap = max(max_gap, bins_min[i]-pre_max)
                pre_max = bins_max[i]

        return max_gap

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""i""m""u""m""G""a""p""(""[""1"","" ""1""0""0""0""]"")"" ""=""="" ""9""9""9