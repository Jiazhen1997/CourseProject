

from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        
        if not nums:
            return 0

        ret = 1
        i = 1
        while i < len(nums):
            cur = 1
            while i < len(nums) and nums[i] > nums[i-1]:
                cur += 1
                i += 1

            i += 1
            ret = max(ret, cur)

        return ret
