

from typing import List
from collections import defaultdict


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        
        h = defaultdict(int)
        m = len(wall)
        for i in range(m):
            s = 0
            for j in range(len(wall[i]) - 1):
                
                s += wall[i][j]
                h[s] += 1

        return m - max(h.values() or [0])
