
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        self.cache = None
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1),)

    def longestIncreasingPath(self, matrix):
        
        if not matrix: return 0

        m, n = len(matrix), len(matrix[0])
        self.cache = [[None for _ in xrange(n)] for _ in xrange(m)]
        gmax = 1
        for i in xrange(m):
            for j in xrange(n):
                gmax = max(gmax, self.longest(matrix, i, j))

        return gmax

    def longest(self, matrix, i, j):
        
        if not self.cache[i][j]:
            m, n = len(matrix), len(matrix[0])
            maxa = 1
            for d in self.dirs:
                I, J = i + d[0], j + d[1]
                if 0 <= I < m and 0 <= J < n and matrix[I][J] > matrix[i][j]:
                    maxa = max(maxa, 1 + self.longest(matrix, I, J))

            self.cache[i][j] = maxa

        return self.cache[i][j]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""I""n""c""r""e""a""s""i""n""g""P""a""t""h""(""[""
"" "" "" "" "" "" "" "" ""[""9"","" ""9"","" ""4""]"",""
"" "" "" "" "" "" "" "" ""[""6"","" ""6"","" ""8""]"",""
"" "" "" "" "" "" "" "" ""[""2"","" ""1"","" ""1""]""
"" "" "" "" ""]"")"" ""=""="" ""4""
