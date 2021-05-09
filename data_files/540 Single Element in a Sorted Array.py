

from typing import List
from bisect import bisect_right


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            if (
                mid % 2 == 0 and mid + 1 < hi and nums[mid] == nums[mid + 1]
            ) or (
                mid % 2 == 1 and mid - 1 >= lo and nums[mid] == nums[mid - 1]
            ):
                
                
                
                lo = mid + 1
            else:
                hi = mid

        return nums[lo]


    def singleNonDuplicate_error(self, nums: List[int]) -> int:
        
        n = len(nums)
        lo, hi = 0, n
        while lo < hi:
            mid = (lo + hi) // 2
            idx = bisect_right(nums, nums[mid], lo, hi)
            if idx <= mid:
                hi = mid - 1
            else:
                lo = mid

        return nums[hi - 1]


    def singleNonDuplicate_xor(self, nums: List[int]) -> int:
        
        ret = nums[0]
        for e in nums[1:]:
            ret ^= e
        return ret
