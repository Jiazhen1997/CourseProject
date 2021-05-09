
__author__ = 'Daniel'


class NumArray(object):
    def __init__(self, nums):
        
        n = len(nums)
        self.F = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            self.F[i] = self.F[i-1] + nums[i-1]

    def sumRange(self, i, j):
        
        return self.F[j+1] - self.F[i]