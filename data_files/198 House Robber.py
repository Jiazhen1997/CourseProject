
__author__ = 'Daniel'


class Solution:
    def rob(self, nums):
        
        n = len(nums)
        f = [0 for _ in xrange(n+2)]
        for i in xrange(2, n+2):
            f[i] = max(
                f[i-1],
                f[i-2] + nums[i-2]
            )

        return f[-1]





