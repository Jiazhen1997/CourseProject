

from typing import List


dirs = ((0, -1), (0, 1), (1, 0), (-1, 0))


class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        
        m, n = len(A), len(A[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and A[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    self.dfs(A, i, j, visited)

        ret = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 1 and not visited[i][j]:
                    ret += 1
        return ret

    def dfs(self, A, i, j, visited):
        m, n = len(A), len(A[0])
        visited[i][j] = True
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n and not visited[I][J] and A[I][J] == 1:
                self.dfs(A, I, J, visited)


class SolutionError:
    def __init__(self):
        self.ret = 0

    def numEnclaves(self, A: List[List[int]]) -> int:
        
        m, n = len(A), len(A[0])
        visited = [[None for _ in range(n)] for _ in range(m)]  
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and A[i][j] == 1:
                    self.dfs(A, i, j, visited)
        return self.ret

    def dfs(self, A, i, j, visited):
        m, n = len(A), len(A[0])
        visited[i][j] = 0
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if not (0 <= I < m and 0 <= J < n):
                visited[i][j] = 1
                return True
            if visited[I][J] == 1:
                visited[i][j] = 1
                return True
            if visited[I][J] is None and A[I][J] == 1 and self.dfs(A, I, J, visited):
                visited[i][j] = 1
                return True

        self.ret += 1
        return False
