

import heapq

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        mxes = heapq.nlargest(3, nums)
        mns = heapq.nsmallest(3, nums)
        return max(
            mxes[0] * mxes[1] * mxes[2],
            mns[0] * mns[1] * mxes[0],
        )
