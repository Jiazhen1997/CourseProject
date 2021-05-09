

__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        self.max = -1
        self.cur_area = 0
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    def solve(self, cipher):
        
        m, n, mat = cipher
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and mat[i][j] == 1:
                    self.cur_area = 0
                    self.dfs(visited, mat, i, j, m, n)

        return self.max

    def dfs(self, visited, mat, i, j, m, n):
        visited[i][j] = True
        self.cur_area += 1
        self.max = max(self.max, self.cur_area)

        for dir in self.dirs:
            i1 = i + dir[0]
            j1 = j + dir[1]
            if 0 <= i1 < m and 0 <= j1 < n and not visited[i1][j1] and mat[i1][j1] == 1:
                self.dfs(visited, mat, i1, j1, m, n)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(