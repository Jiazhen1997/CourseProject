
__author__ = 'Daniel'


class Solution:
    def rotate(self, nums, k):
        
        n = len(nums)
        k %= n
        temp = nums[:n-k]
        for i in xrange(n):
            if i < k:
                nums[i] = nums[n-k+i]
            else:
                nums[i] = temp[i-k]

