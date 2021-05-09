

__author__ = 'Daniel'


class NumMatrix(object):
    def __init__(self, matrix):
        
        m = len(matrix)
        if m == 0:
            self.F = None
            return

        n = len(matrix[0])
        self.F = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                self.F[i][j] = self.F[i-1][j]+self.F[i][j-1]-self.F[i-1][j-1]+matrix[i-1][j-1]

    def sumRegion(self, row1, col1, row2, col2):
        
        if not self.F:
            return 0

        return self.F[row2+1][col2+1] - self.F[row2+1][col1] - self.F[row1][col2+1] + self.F[row1][col1]