
__author__ = 'Danyang'
class Solution:
    def setZeroes_error(self, matrix):
        
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        for row in xrange(m):
            for col in xrange(n):
                if matrix[row][col]==0:
                    matrix[0][col]=0  
                    matrix[row][0]=0  

        for row in xrange(m):
            if matrix[row][0]==0:
                for col in xrange(n):
                    matrix[row][col] = 0

        for col in xrange(n):
            if matrix[0][col]==0:
                for row in xrange(m):
                    matrix[row][col] = 0


    def setZeroes(self, matrix):
        
        if not matrix:
            return

        m = len(matrix)
        n = len(matrix[0])

        
        clear_first_row = False
        clear_first_col = False
        for row in xrange(m):
            if matrix[row][0]==0:
                clear_first_col = True
        for col in xrange(n):
            if matrix[0][col]==0:
                clear_first_row = True

        for row in xrange(1, m):
            for col in xrange(1, n):
                if matrix[row][col]==0:
                    matrix[0][col] = 0  
                    matrix[row][0] = 0  

        for row in xrange(1, m):  
            if matrix[row][0]==0:
                for col in xrange(n):
                    matrix[row][col] = 0

        for col in xrange(1, n):  
            if matrix[0][col]==0:
                for row in xrange(m):
                    matrix[row][col] = 0

        if clear_first_row:
            for col in xrange(n):
                matrix[0][col] = 0
        if clear_first_col:
            for row in xrange(m):
                matrix[row][0] = 0



