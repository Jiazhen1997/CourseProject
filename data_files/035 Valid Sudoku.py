
__author__ = 'Danyang'
class Solution:
    def isValidSudoku(self, board):
        
        
        for i in xrange(9):
            row = []  
            column = []
            square = []
            for j in xrange(9):
                
                try:
                    row_element = int(board[i][j])
                    if row_element in row:
                        return False
                    else:
                        row.append(row_element)
                except ValueError:
                    pass

                
                try:
                    column_element = int(board[j][i])
                    if column_element in column:
                        return False
                    else:
                        column.append(column_element)
                except ValueError:
                    pass

                
                try:
                    square_element = int(board[i/3*3 + j/3][i%3*3 + j%3])
                    if square_element in square:
                        return False
                    else:
                        square.append(square_element)
                except ValueError:
                    pass

        return True

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""V""a""l""i""d""S""u""d""o""k""u""(""
"" "" "" "" "" "" "" "" ""[