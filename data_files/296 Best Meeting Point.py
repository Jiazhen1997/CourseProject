
__author__ = 'Daniel'


class Solution(object):
    def minTotalDistance_3lines(self, grid):
        x = sorted([i for i, row in enumerate(grid) for v in row if v == 1])
        y = sorted([j for row in grid for j, v in enumerate(row) if v == 1])
        return sum([abs(x[len(x)/2]-i)+abs(y[len(y)/2]-j) for i, row in enumerate(grid) for j, v in enumerate(row) if v == 1])

    def minTotalDistance(self, grid):
        
        x = []
        y = []

        m = len(grid)
        n = len(grid[0])
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    x.append(i)
                    y.append(j)

        x.sort()
        y.sort()
        cnt = len(x)
        point = (x[cnt/2], y[cnt/2])
        ret = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == 1:
                    ret += abs(point[0]-i)
                    ret += abs(point[1]-j)

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""T""o""t""a""l""D""i""s""t""a""n""c""e""(""[""[""1"",""0"",""0"",""0"",""1""]"",""[""0"",""0"",""0"",""0"",""0""]"",""[""0"",""0"",""1"",""0"",""0""]""]"")"" ""=""="" ""6