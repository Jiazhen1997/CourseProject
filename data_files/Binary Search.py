
__author__ = 'Danyang'


class Solution:
    def binarySearch(self, nums, target):
        
        l = 0
        h = len(nums)
        while l < h:
            mid = (l+h)/2
            if nums[mid] == target:
                while mid >= 0 and nums[mid-1] == nums[mid]: mid -= 1
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                h = mid
        return -1

