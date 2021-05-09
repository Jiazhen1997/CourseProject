
__author__ = 'Danyang'
INVALID = -1
QUEEN = 1
DEFAULT = 0
directions = [(+1, +1), (-1, -1), (-1, +1), (+1, -1)]
class Solution:
    def solveNQueens(self, n):
        
        result = []
        current = [[0 for _ in xrange(n)] for _ in xrange(n)]
        self.backtrack(0, current, result)
        return self.transform2string(result)

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

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

                
                for direction in directions:
                    row = queen_index+direction[0]*m
                    col = i+direction[1]*m
                    if 0<=row<n and 0<=col<n and new_config[row][col]==DEFAULT:
                        new_config[row][col] = INVALID

            
            
            self.backtrack(queen_index+1, new_config, result)


    def transform2string(self, result):
        string_result = []
        for configuration in result:
            current = []
            for row in configuration:
                row = map(lambda x: "."" ""i""f"" ""x""=""=""-""1"" ""e""l""s""e"" 