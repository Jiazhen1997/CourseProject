

from typing import List


dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        
        m, n = len(A), len(A[0])
        
        colors = [[None for _ in range(n)] for _ in range(m)]
        color = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and colors[i][j] is None:
                    self.dfs(A, i, j, colors, color)
                    color += 1
        assert color == 2

        
        step = 0
        q = []
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if colors[i][j] == 0:
                    visited[i][j] = True
                    q.append((i, j))

        while q:
            cur_q = []
            for i, j in q:
                for I, J in self.nbr(A, i, j):
                    if not visited[I][J]:
                        if colors[I][J] == None:
                            visited[I][J] = True   
                            cur_q.append((I, J))
                        elif colors[I][J] == 1:
                            return step
            step += 1
            q = cur_q

        raise

    def nbr(self, A, i, j):
        m, n = len(A), len(A[0])
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n:
                yield I, J

    def dfs(self, A, i, j, colors, color):
        colors[i][j] = color
        for I, J in self.nbr(A, i, j):
            if colors[I][J] is None and A[I][J] == 1:
                self.dfs(A, I, J, colors, color)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""h""o""r""t""e""s""t""B""r""i""d""g""e""(""[""[""1"",""1"",""1"",""1"",""1""]"",""[""1"",""0"",""0"",""0"",""1""]"",""[""1"",""0"",""1"",""0"",""1""]"",""[""1"",""0"",""0"",""0"",""1""]"",""[""1"",""1"",""1"",""1"",""1""]""]"")"" ""=""="" ""1""
