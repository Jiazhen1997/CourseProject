
__author__ = 'Danyang'
class Solution:
    def exist(self, board, word):
        
        if not board:
            return
        
        

        m = len(board)
        n = len(board[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]  
        for i in xrange(m):
            for j in xrange(n):
                if board[i][j]==word[0]:
                    visited[i][j] = True
                    if self.search(board, i, j, word[1:], visited):
                        return True
                    visited[i][j] = False
        return False

    def search(self, board, pre_row, pre_col, word, visited):
        if not word:
            return True
        
        m = len(board)
        n = len(board[0])
        next_positions = [(pre_row-1, pre_col), (pre_row+1, pre_col), (pre_row, pre_col-1), (pre_row, pre_col+1)]  
        for next_position in next_positions:
            if 0<=next_position[0]<m and 0<=next_position[1]<n:  
                if visited[next_position[0]][next_position[1]]==False and board[next_position[0]][next_position[1]]==word[0]:
                    visited[next_position[0]][next_position[1]] = True
                    if self.search(board, next_position[0], next_position[1], word[1:], visited):
                        return True
                    visited[next_position[0]][next_position[1]] = False  
        return False



if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""b""o""a""r""d"" ""="" ""[""
"" "" "" "" "" "" "" "" 