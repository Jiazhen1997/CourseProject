

from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True

    def isToeplitzMatrix_complex(self, matrix: List[List[int]]) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        for j in range(n):
            r = 0
            c = j
            cur = matrix[r][c]
            while r < m and c < n:
                if cur != matrix[r][c]:
                    return False
                r += 1
                c += 1

        for i in range(1, m):
            r = i
            c = 0
            cur = matrix[r][c]
            while r < m and c < n:
                if cur != matrix[r][c]:
                    return False

                r += 1
                c += 1

        return True
