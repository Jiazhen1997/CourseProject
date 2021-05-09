


__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.dirs = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

    def gameOfLife(self, board):
        
        m = len(board)
        n = len(board[0])
        lines = [[0 for _ in xrange(n)] for _ in xrange(2)]
        for i in xrange(m):
            for j in xrange(n):
                lines[(i+1)%2][j] = board[i][j]

                cnt = 0
                for d in self.dirs:
                    I = i+d[0]
                    J = j+d[1]
                    if 0 <= I < m and 0 <= J < n:
                        if I < i:
                            cnt += lines[i%2][J]
                        elif I == i and J < j:
                            cnt += lines[(i+1)%2][J]
                        else:
                            cnt += board[I][J]

                if cnt == 3:
                    board[i][j] = 1
                elif cnt == 2:
                    board[i][j] &= 1
                else:
                    board[i][j] = 0
