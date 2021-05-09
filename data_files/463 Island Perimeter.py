

class Solution:
    dirs = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def islandPerimeter(self, grid):
        
        ret = 0
        if not grid:
            return ret
        R = len(grid)
        C = len(grid[0])
        for r0 in range(R):
            for c0 in range(C):
                if grid[r0][c0] == 1:
                    for dr, dc in self.dirs:
                        r = r0 + dr
                        c = c0 + dc
                        if r < 0 or r >= R or c < 0 or c >= C:
                            ret += 1
                        elif grid[r][c] == 0:
                            ret += 1

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""g""r""i""d"" ""="" ""[""
"" "" "" "" "" "" "" "" ""[""0"",""1"",""0"",""0""]"",""
"" "" "" "" "" "" "" "" ""[""1"",""1"",""1"",""0""]"",""
"" "" "" "" "" "" "" "" ""[""0"",""1"",""0"",""0""]"",""
"" "" "" "" "" "" "" "" ""[""1"",""1"",""0"",""0""]"",""
"" "" "" "" ""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""l""a""n""d""P""e""r""i""m""e""t""e""r""(""g""r""i""d"")"" ""=""="" ""1""6""
