

from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(nums), len(nums[0])
        if m * n != r * c:
            return nums

        ret = []
        for i in range(m):
            for j in range(n):
                if (i * n + j) % c == 0:
                    ret.append([])
                ret[-1].append(nums[i][j])

        return ret 
