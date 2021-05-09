

from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        lr = [
            max(row)
            for row in grid
        ]
        
        tb = [
            max(
                grid[i][j]
                for i in range(m)
            )
            for j in range(n)
        ]

        ret = 0
        for i in range(m):
            for j in range(n):
                diff = min(lr[i], tb[j]) - grid[i][j]
                ret += diff

        return ret
