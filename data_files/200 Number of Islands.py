
__author__ = 'Daniel'


class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def numIslands(self, grid):
        
        m = len(grid)
        if m < 1:
            return 0
        n = len(grid[0])
        if n < 1:
            return 0

        cnt = 0
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if not visited[i][j] and grid[i][j] == "1"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""g""r""i""d"","" ""i"","" ""j"","" ""v""i""s""i""t""e""d"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""n""t"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""c""n""t""
""
"" "" "" "" ""d""e""f"" ""d""f""s""(""s""e""l""f"","" ""g""r""i""d"","" ""i"","" ""j"","" ""v""i""s""i""t""e""d"")"":""
"" "" "" "" "" "" "" "" 
        m = len(grid)
        n = len(grid[0])
        visited[i][j] = True

        for dir in self.dirs:
            I = i+dir[0]
            J = j+dir[1]
            if 0 <= I < m and 0 <= J < n and not visited[I][J] and grid[I][J] == "1"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""d""f""s""(""g""r""i""d"","" ""I"","" ""J"","" ""v""i""s""i""t""e""d"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 