
__author__ = 'Danyang'
INVALID = -1
QUEEN = 1
DEFAULT = 0
class Solution:
    def totalNQueens(self, n):
        
        result = []
        current = [[0 for _ in xrange(n)] for _ in xrange(n)]
        self.backtrack(0, current, result)
        return len(result)

    def backtrack(self, queen_index, current, result):
        
        n = len(current)
        if queen_index==n:
            result.append(current)
            return

        for i in xrange(n):
            if current[queen_index][i]==INVALID:
                continue

            
            new_config = [list(element) for element in current]  
            new_config[queen_index][i] = QUEEN

            
            for m in xrange(n):
                
                if new_config[m][i]==DEFAULT:
                    new_config[m][i] = INVALID
                    
                if new_config[queen_index][m]==DEFAULT:
                    new_config[queen_index][m] = INVALID

                
                row = queen_index+m
                col = i+m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

                row = queen_index-m
                col = i-m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

                row = queen_index-m
                col = i+m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

                row = queen_index+m
                col = i-m
                if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT: new_config[row][col] = INVALID

            self.backtrack(queen_index+1, new_config, result)


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""t""o""t""a""l""N""Q""u""e""e""n""s""(""4"")