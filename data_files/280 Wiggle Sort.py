
__author__ = 'Daniel'


class Solution(object):
    def wiggleSort(self, nums):
        
        i = 0
        for elt in sorted(nums):
            if i >= len(nums):
                i = 1
            nums[i] = elt
            i += 2
