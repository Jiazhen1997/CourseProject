
__author__ = 'Daniel'


class Solution(object):
    def __init__(self):
        
        self.skip = [[None for _ in xrange(10)] for _ in xrange(10)]
        self.skip[1][3], self.skip[3][1] = 2, 2
        self.skip[1][7], self.skip[7][1] = 4, 4
        self.skip[3][9], self.skip[9][3] = 6, 6
        self.skip[7][9], self.skip[9][7] = 8, 8
        self.skip[4][6], self.skip[6][4] = 5, 5
        self.skip[2][8], self.skip[8][2] = 5, 5
        self.skip[1][9], self.skip[9][1] = 5, 5
        self.skip[3][7], self.skip[7][3] = 5, 5

    def numberOfPatterns(self, m, n):
        
        visited = [False for _ in xrange(10)]
        return sum(
            self.dfs(1, visited, remain) * 4 +
            self.dfs(2, visited, remain) * 4 +
            self.dfs(5, visited, remain)
            for remain in xrange(m, n+1)
        )

    def dfs(self, cur, visited, remain):
        
        if remain == 1:
            return 1

        visited[cur] = True
        ret = 0
        for nxt in xrange(1, 10):
            if (
                not visited[nxt] and (
                    self.skip[cur][nxt] is None or
                    visited[self.skip[cur][nxt]]
                )
            ):
                ret += self.dfs(nxt, visited, remain - 1)

        visited[cur] = False
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""b""e""r""O""f""P""a""t""t""e""r""n""s""(""1"","" ""2"")"" ""=""="" ""6""5""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""b""e""r""O""f""P""a""t""t""e""r""n""s""(""1"","" ""3"")"" ""=""="" ""3""8""5""
