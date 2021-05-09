

from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        i = 0
        ret = 0
        p = 1
        for j in range(len(nums)):
            p *= nums[j]
            while p >= k and i <= j:
                p //= nums[i]
                i += 1

            ret += j - i + 1  
            

        return ret
