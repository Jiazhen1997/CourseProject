

from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        acc0 = 0  
        for i in range(n):
            acc0 ^= nums[i]
            acc0 ^= i + 1

        first_1 = acc0 & - acc0  
        
        
        acc1 = 0
        acc2 = 0
        for i in range(n):
            if nums[i] & first_1:
                acc1 ^= nums[i]
            else:
                acc2 ^= nums[i]

            if (i + 1) & first_1:
                acc1 ^= i + 1
            else:
                acc2 ^= i + 1

        for i in range(n):
            if nums[i] == acc1:
                return [acc1, acc2]

        return [acc2, acc1]
