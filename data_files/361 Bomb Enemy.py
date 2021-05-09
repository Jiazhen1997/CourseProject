
__author__ = 'Daniel'


class Solution(object):
    def maxKilledEnemies(self, grid):
        
        if not grid: return 0

        m, n = len(grid), len(grid[0])
        rows = [0 for _ in xrange(m)]
        cols = [0 for _ in xrange(n)]
        gmax = 0
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or grid[i-1][j] == 'W':
                    cols[j] = 0
                    for k in xrange(i, m):
                        if grid[k][j] == 'E':
                            cols[j] += 1
                        elif grid[k][j] == 'W':
                            break

                if j == 0 or grid[i][j-1] == 'W':
                    rows[i] = 0
                    for k in xrange(j, n):
                        if grid[i][k] == 'E':
                            rows[i] += 1
                        elif grid[i][k] == 'W':
                            break

                if grid[i][j] == '0':
                    gmax = max(gmax, rows[i] + cols[j])

        return gmax

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""K""i""l""l""e""d""E""n""e""m""i""e""s""(""[