
__author__ = 'Danyang'
class Solution:
    def solveSudoku(self, board):
        
        
        for row in xrange(len(board)):
            board[row] = list(board[row])
        self.solve(board, 0, 0)
        for row in xrange(len(board)):
            board[row] = "".""j""o""i""n""(""b""o""a""r""d""[""r""o""w""]"")""
""
"" "" "" "" ""d""e""f"" ""s""o""l""v""e""_""T""L""E""(""s""e""l""f"","" ""b""o""a""r""d"")"":""
"" "" "" "" "" "" "" "" 
        n = len(board)
        if all([board[i/n][i%n]!="."" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""n""*""n"")""]"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""n"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""x""r""a""n""g""e""(""n"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""b""o""a""r""d""[""i""]""[""j""]""=""=
        dfs
        :param board: a 9x9 2D array
        :return: Boolean
        