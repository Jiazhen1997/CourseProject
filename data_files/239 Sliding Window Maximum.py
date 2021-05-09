

__author__ = 'Daniel'


class Solution:
    def maxSlidingWindow(self, nums, k):
        
        q = []  
        ret = []
        n = len(nums)
        for i in xrange(n):
            while q and q[0] <= i-k:
                q.pop(0)
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            if i >= k-1:
                ret.append(nums[q[0]])

        return ret
