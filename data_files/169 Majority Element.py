

__author__ = 'Daniel'


class Solution:
    def majorityElement(self, nums):
        
        mjr = nums[0]
        cnt = 0
        for i, v in enumerate(nums):
            if mjr == v:
                cnt += 1
            else:
                cnt -= 1

            if cnt < 0:
                mjr = v
                cnt = 1

        return mjr

