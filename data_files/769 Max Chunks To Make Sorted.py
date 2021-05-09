

from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        ret = 0
        cur_max_idx = 0
        for i in range(len(arr)):
            cur_max_idx = max(cur_max_idx, arr[i])
            if i == cur_max_idx:
                ret += 1

        return ret
