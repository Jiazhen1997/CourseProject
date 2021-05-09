
__author__ = 'Daniel'


class Solution:
    def rob(self, nums):
        
        n = len(nums)
        if n < 2:
            return sum(nums)

        
        F = [0 for _ in xrange(n-1+2)]
        for i in xrange(2, n+1):
            F[i] = max(F[i-1], F[i-2]+nums[i-2])
        ret = F[-1]

        
        F = [0 for _ in xrange(n-1+2)]
        for i in xrange(2, n+1):
            F[i] = max(F[i-1], F[i-2]+nums[i-1])

        ret = max(ret, F[-1])
        return ret
