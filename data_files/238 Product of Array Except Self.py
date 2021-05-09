
__author__ = 'Daniel'


class Solution:
    def productExceptSelf(self, nums):
        
        n = len(nums)
        left = [1 for _ in xrange(n+1)]  
        right = [1 for _ in xrange(n+1)]  
        for i in xrange(1, n+1):
            left[i] = left[i-1]*nums[i-1]
        for i in xrange(n-1, -1, -1):
            right[i] = right[i+1]*nums[i]

        return [left[i]*right[i+1] for i in xrange(n)]