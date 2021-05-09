

from typing import List
from collections import defaultdict
from copy import deepcopy
import heapq


final_pos = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    0: (1, 2),
}

dirs = (
    (0, -1),
    (0, 1),
    (-1, 0),
    (1, 0),
)


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        
        visited = defaultdict(bool)
        m, n = len(board), len(board[0])
        q = [(self.heuristic_dist(board) + 0, 0, board)]
        target = [
            [1, 2, 3],
            [4, 5, 0],
        ]
        while q:
            heu, cur_dist, board = heapq.heappop(q)
            visited[self.ser(board)] = True
            if board == target:
                return cur_dist

            cur_dist += 1
            i, j = self.zero_pos(board)
            for di, dj in dirs:
                I = i + di
                J = j + dj
                if 0 <= I < m and 0 <= J < n:
                    B = deepcopy(board)   
                    B[I][J], B[i][j] = B[i][j], B[I][J]
                    if not visited[self.ser(B)]:
                        heapq.heappush(q, (self.heuristic_dist(B) + cur_dist, cur_dist, B))
        return -1

    def zero_pos(self, board):
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == 0:
                    return i, j
        raise

    def heuristic_dist(self, board):
        
        ret = 0
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v != 0:
                    I, J = final_pos[v]
                    ret += abs(i - I) + abs(j - J)
        return ret

    def ser(self, board):
        return tuple(
            tuple(row)
            for row in board
        )


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""l""i""d""i""n""g""P""u""z""z""l""e""(""[""[""1"",""2"",""3""]"",""[""4"",""0"",""5""]""]"")"" ""=""="" ""1""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""l""i""d""i""n""g""P""u""z""z""l""e""(""[""[""1"",""2"",""3""]"",""[""5"",""4"",""0""]""]"")"" ""=""="" ""-""1""
