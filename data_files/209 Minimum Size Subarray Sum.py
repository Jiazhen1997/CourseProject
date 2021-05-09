

__author__ = 'Daniel'
import sys


class Solution:
    def minSubArrayLen(self, s, nums):
        
        n = len(nums)

        S = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            S[i] = S[i-1]+nums[i-1]

        lo, hi = 0, 1
        mini = sys.maxint
        while hi <= n:
            if S[hi]-S[lo] >= s:
                mini = min(mini, hi-lo)
                lo += 1
            else:
                hi += 1

        return mini if mini != sys.maxint else 0


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""S""u""b""A""r""r""a""y""L""e""n""(""7"","" ""[""2"","" ""3"","" ""1"","" ""2"","" ""4"","" ""3""]"")"" ""=""="" ""2""
""
