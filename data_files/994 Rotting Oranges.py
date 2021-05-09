

from typing import List


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))

        t = -1
        while q:
            t += 1
            cur_q = []
            for i, j in q:
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < m and 0 <= J < n and grid[I][J] == 1:
                        grid[I][J] = 2
                        cur_q.append((I, J))
            q = cur_q

        has_fresh = any(
            grid[i][j] == 1
            for i in range(m)
            for j in range(n)
        )

        return max(0, t) if not has_fresh else -1
