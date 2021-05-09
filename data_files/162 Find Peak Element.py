

__author__ = 'Daniel'
import sys


class Solution:
    def __init__(self):
        self.A = None

    def findPeakElement(self, nums):
        
        self.A = nums
        n = len(self.A)
        if n < 2:
            return 0

        l = 0
        h = n
        while l < h:
            m = (l+h)/2
            if self._get(m-1) < self._get(m) > self._get(m+1):
                return m
            elif self._get(m+1) > self._get(m):
                l = m+1
            else:
                h = m

        return -1

    def _get(self, i):
        if i < 0 or i >= len(self.A):
            return -sys.maxint-1
        else:
            return self.A[i]

    def findPeakElement_complicated(self, nums):
        
        n = len(nums)
        if n < 2:
            return 0

        l = 0
        h = n
        while l < h:
            m = (l+h)/2
            if m == 0 and nums[m] > nums[m+1]:
                return m
            elif m == n-1 and nums[m] > nums[m-1]:
                return m
            elif nums[m-1] < nums[m] > nums[m+1]:
                return m

            elif m+1 < n and nums[m+1] > nums[m]:
                l = m+1
            else:
                h = m

        return -1