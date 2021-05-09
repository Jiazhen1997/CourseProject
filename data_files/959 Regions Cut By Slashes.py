

from typing import List


class DisjointSet:
    def __init__(self):
        
        self.pi = {}

    def union(self, x, y):
        pi_x = self.find(x)
        pi_y = self.find(y)
        self.pi[pi_y] = pi_x

    def find(self, x):
        
        if x not in self.pi:
            self.pi[x] = x
        if self.pi[x] != x:
            self.pi[x] = self.find(self.pi[x])
        return self.pi[x]

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        m, n = len(grid), len(grid[0])
        ds = DisjointSet()
        T, R, B, L = range(4)  
        for i in range(m):
            for j in range(n):
                e = grid[i][j]
                if e == "/"" ""o""r"" ""e"" ""=""="" 