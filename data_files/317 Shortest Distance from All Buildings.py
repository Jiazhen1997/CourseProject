
import sys

__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def shortestDistance(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        acc = [[0 for _ in xrange(n)] for _ in xrange(m)]
        reachable = [[True for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] > 0:
                    reachable[i][j] = False
                    acc[i][j] = sys.maxint

        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    self.bfs(grid, acc, reachable, i, j)

        mini = sys.maxint
        for i in xrange(m):
            for j in xrange(n):
                if acc[i][j] < mini and reachable[i][j]:
                    mini = acc[i][j]

        return mini if mini != sys.maxint else -1

    def bfs(self, grid, acc, reachable, x, y):
        d = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]

        q = [(x, y)]
        visited[x][y] = True  
        while q:
            l = len(q)
            for idx in xrange(l):
                i, j = q[idx]
                acc[i][j] += d

                for dir in self.dirs:
                    I = i+dir[0]
                    J = j+dir[1]
                    if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                        q.append((I, J))
                        visited[I][J] = True

            d += 1
            q = q[l:]

        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j]:
                    reachable[i][j] = False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""h""o""r""t""e""s""t""D""i""s""t""a""n""c""e""(""
"" "" "" "" "" "" "" "" ""[""[""1"","" ""1"","" ""1"","" ""1"","" ""1"","" ""0""]"","" ""[""0"","" ""0"","" ""0"","" ""0"","" ""0"","" ""1""]"","" ""[""0"","" ""1"","" ""1"","" ""0"","" ""0"","" ""1""]"","" ""[""1"","" ""0"","" ""0"","" ""1"","" ""0"","" ""1""]"","" ""[""1"","" ""0"","" ""1"","" ""0"","" ""0"","" ""1""]"",""
"" "" "" "" "" "" "" "" "" ""[""1"","" ""0"","" ""0"","" ""0"","" ""0"","" ""1""]"","" ""[""0"","" ""1"","" ""1"","" ""1"","" ""1"","" ""0""]""]"")"" ""=""="" ""8""8""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""h""o""r""t""e""s""t""D""i""s""t""a""n""c""e""(""[""[""1"","" ""2"","" ""0""]""]"")"" ""=""="" ""-""1""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""h""o""r""t""e""s""t""D""i""s""t""a""n""c""e""(""[""[""1"","" ""0"","" ""2"","" ""0"","" ""1""]"","" ""[""0"","" ""0"","" ""0"","" ""0"","" ""0""]"","" ""[""0"","" ""0"","" ""1"","" ""0"","" ""0""]""]"")"" ""=""="" ""7""
