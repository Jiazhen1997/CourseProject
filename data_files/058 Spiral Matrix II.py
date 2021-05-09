
__author__ = 'Danyang'


class Solution:
    def generateMatrix(self, n):
        
        left = 0
        right = n - 1 
        top = 0
        bottom = n - 1  

        result = [[-1 for _ in xrange(n)] for _ in xrange(n)]
        num = 1
        while left <= right and top <= bottom:
            for i in xrange(left, right + 1):  
                result[top][i] = num
                num += 1
            for i in xrange(top + 1, bottom):
                result[i][right] = num
                num += 1

            for i in xrange(right, left, -1):
                result[bottom][i] = num
                num += 1
            for i in xrange(bottom, top, -1):
                result[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result


class SolutionError:
    def generateMatrix(self, n):
        
        left = 0
        right = n - 1 
        top = 0
        bottom = n - 1  

        result = [[-1 for _ in xrange(n)] for _ in xrange(n)]
        num = 1
        while left <= right and top <= bottom:
            for i in xrange(left, right):  
                result[top][i] = num
                num += 1
            for i in xrange(top, bottom):
                result[i][right] = num
                num += 1

            for i in xrange(right, left, -1):
                result[bottom][i] = num
                num += 1

            for i in xrange(bottom, top, -1):
                result[i][left] = num
                num += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""r""e""s""u""l""t"" ""="" ""S""o""l""u""t""i""o""n""("")"".""g""e""n""e""r""a""t""e""M""a""t""r""i""x""(""4"")""
"" "" "" "" ""f""o""r"" ""r""o""w"" ""i""n"" ""r""e""s""u""l""t"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""r""o""w""
