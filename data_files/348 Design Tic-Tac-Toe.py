
__author__ = 'Daniel'


class TicTacToe(object):
    def __init__(self, n):
        
        self.n = n
        self.rows_count = [0 for _ in xrange(n)]
        self.cols_count = [0 for _ in xrange(n)]
        self.diag_count = 0
        self.diag_inv_count = 0

    def move(self, row, col, player):
        
        delta = -1 if player == 1 else 1
        self.cols_count[col] += delta
        self.rows_count[row] += delta
        if col == row:
            self.diag_count += delta
        if col + row == self.n - 1:
            self.diag_inv_count += delta

        
        is_win = lambda count: delta * count == self.n
        if any(map(is_win, [self.rows_count[row], self.cols_count[col], self.diag_count, self.diag_inv_count])):
            return player

        return 0




