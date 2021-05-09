
__author__ = 'Danyang'
class Solution:
    def generate(self, numRows):
        
        result = []
        for row in xrange(numRows):
            current = []
            for col in xrange(row+1):
                if col==0 or col==row:
                    current.append(1)
                else:
                    current.append(result[row-1][col-1]+result[row-1][col])
            result.append(current)

        return result

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""g""e""n""e""r""a""t""e""(""5"")