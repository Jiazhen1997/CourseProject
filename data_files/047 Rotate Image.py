
__author__ = 'Danyang'
class Solution:
    def rotate(self, matrix):
        
        n = len(matrix)
        for row in range(n):
            for col in range(n-row):
                matrix[row][col], matrix[n-1-col][n-1-row] = matrix[n-1-col][n-1-row], matrix[row][col]  
        for row in range(n/2):
            for col in range(n):
                matrix[row][col], matrix[n-1-row][col] = matrix[n-1-row][col], matrix[row][col]  

        return matrix




