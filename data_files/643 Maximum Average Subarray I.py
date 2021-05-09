

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        cur_sum = sum(nums[:k])
        maxa = cur_sum
        i = k
        while i < len(nums):
            cur_sum += nums[i]
            cur_sum -= nums[i-k]
            maxa = max(maxa, cur_sum)
            i += 1

        return maxa / k
