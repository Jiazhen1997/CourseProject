
__author__ = 'Daniel'


class Solution:
    def printZMatrix(self, matrix):
        
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        ret = []

        up = True
        for _ in xrange(m*n):
            ret.append(matrix[i][j])
            if up:
                if i-1<0 or j+1>=n:
                    up = False
                    if j+1>=n:  
                        i += 1
                    else:  
                        j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i+1>=m or j-1<0:
                    up = True
                    if i+1>=m:
                        j += 1  
                    else:
                        i += 1  
                else:
                    i += 1
                    j -= 1

        return ret

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""m""a""t""r""i""x"" ""="" ""[""
"" "" "" "" "" "" "" "" ""[""1"","" ""2"","" ""3"","" ""4""]"",""
"" "" "" "" "" "" "" "" ""[""5"","" ""6"","" ""7"","" ""8""]"",""
"" "" "" "" "" "" "" "" ""[""9"","" ""1""0"","" ""1""1"","" ""1""2""]""
"" "" "" "" ""]""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""p""r""i""n""t""Z""M""a""t""r""i""x""(""m""a""t""r""i""x"")""
