
__author__ = 'Daniel'


class Solution:
    def __init__(self):
        self.dirs = [[0, -1], [0, 1], [1, 0], [-1, 0]]

    def numIslands(self, grid):
        
        if not grid: return 0
        m = len(grid)
        if not m: return 0
        n = len(grid[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        cnt = 0
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and grid[i][j]:
                    cnt += 1
                    self.dfs(grid, i, j, visited)

        return cnt

    def dfs(self, grid, i, j, visited):
        
        m = len(grid)
        n = len(grid[0])
        visited[i][j] = True
        for dir in self.dirs:
            i1 = i+dir[0]
            j1 = j+dir[1]
            if 0 <= i1 < m and 0 <= j1 < n and not visited[i1][j1] and grid[i1][j1]:
                self.dfs(grid, i1, j1, visited)
