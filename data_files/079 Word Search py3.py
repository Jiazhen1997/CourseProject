

from typing import List
from collections import defaultdict


dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = defaultdict(lambda: defaultdict(bool))
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if self.dfs(board, visited, i, j, word, 1):
                        return True

        return False

    def dfs(self, board, visited, i, j, word, idx):
        visited[i][j] = True
        if idx >= len(word):
            return True

        m, n = len(board), len(board[0])
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n and not visited[I][J] and board[I][J] == word[idx]:
                if self.dfs(board, visited, I, J, word, idx + 1):
                    return True

        visited[i][j] = False  
        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""e""x""i""s""t""(""[""
"" "" "" "" "" "" "" "" ""[