
__author__ = 'Danyang'


class Solution:
    def spiralOrder(self, matrix):
        
        if not matrix or not matrix[0]:
            return matrix

        result = []

        left = 0
        right = len(matrix[0]) - 1
        top = 0
        bottom = len(matrix) - 1

        while left <= right and top <= bottom:
            for c in xrange(left, right + 1):
                result.append(matrix[top][c])
            for r in xrange(top + 1, bottom + 1):
                result.append(matrix[r][right])
            for c in xrange(right - 1, left - 1, -1):
                if top < bottom:  
                    result.append(matrix[bottom][c])
            for r in xrange(bottom - 1, top, -1):
                if left < right:  
                    result.append(matrix[r][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""s""p""i""r""a""l""O""r""d""e""r""(""[""[""2"","" ""3""]""]"")""
