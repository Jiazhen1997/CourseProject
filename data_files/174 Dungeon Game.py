
__author__ = 'Daniel'
import sys


class Solution:
    def calculateMinimumHP(self, dungeon):
        
        m = len(dungeon)
        n = len(dungeon[0])

        F = [[sys.maxint for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(m-1, -1, -1):
            for j in xrange(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    F[i][j] = max(1, 1-dungeon[i][j])
                else:
                    path = min(F[i+1][j], F[i][j+1])  
                    F[i][j] = max(1, path-dungeon[i][j])  

        return F[0][0]

    def calculateMinimumHP_error(self, dungeon):
        
        m = len(dungeon)
        n = len(dungeon[0])
        if m == 1 and n == 1:
            return 1-min(0, dungeon[0][0])

        F = [[-sys.maxint-1 for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if i == 1 and j == 1:
                    F[i][j] = dungeon[i-1][j-1]
                else:
                    F[i][j] = max(F[i-1][j], F[i][j-1])+dungeon[i-1][j-1]
                    F[i][j] = min(F[i][j], dungeon[i-1][j-1])

        return 1-F[-1][-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""l""c""u""l""a""t""e""M""i""n""i""m""u""m""H""P""(""[""[""-""3"","" ""5""]""]"")"" ""=""="" ""4""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""l""c""u""l""a""t""e""M""i""n""i""m""u""m""H""P""(""[""[""2"","" ""1""]"","" ""[""1"","" ""-""1""]""]"")"" ""=""="" ""1""
