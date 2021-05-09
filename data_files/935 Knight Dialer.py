



MOD = 10 ** 9 + 7


dirs = [
    (-2, 1),
    (-1, 2),
    (1, 2),
    (2, 1),
    (2, -1),
    (1, -2),
    (-1, -2),
    (-2, -1),
]

nbrs = {
    1: (6, 8),
    2: (7, 9),
    3: (4, 8),
    4: (3, 9, 0),
    5: tuple(),
    6: (1, 7, 0),
    7: (2, 6),
    8: (1, 3),
    9: (2, 4),
    0: (4, 6),
}


from collections import defaultdict


class Solution:
    def knightDialer(self, N: int) -> int:
        
        F = defaultdict(lambda: defaultdict(int))
        for pos in range(10):
            F[pos][N-1] = 1

        for n in range(N-2, -1, -1):
            for pos in range(10):
                for nbr in nbrs[pos]:
                    F[pos][n] += F[nbr][n+1]
                    F[pos][n] %= MOD

        ret = 0
        for i in range(10):
            ret += F[i][0]
            ret %= MOD

        return ret


class SolutionTLE2:
    def __init__(self):
        self.cache = {}

    def knightDialer(self, N: int) -> int:
        ret = 0
        for i in range(10):
            ret += self.dfs(i, N-1)
            ret %= MOD

        return ret

    def dfs(self, i, r):
        if (i, r) not in self.cache:
            ret = 0
            if r == 0:
                ret = 1
            else:
                for nbr in nbrs[i]:
                    ret += self.dfs(nbr, r-1)

            self.cache[i, r] = ret

        return self.cache[i, r]


class SolutionTLE:
    def __init__(self):
        
        self.m = 4
        self.n = 3
        self.cache = {}

    def knightDialer(self, N: int) -> int:
        ret = 0
        for i in range(self.m):
            for j in range(self.n):
                if (i, j) != (3, 0) and (i, j) != (3, 2):
                    ret += self.dfs(i, j, N-1)
                    ret %= MOD
        return ret

    def dfs(self, i, j, r):
        if (i, j, r) not in self.cache:
            ret = 0
            if r == 0:
                ret = 1
            else:
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < self.m and 0 <= J < self.n and (I, J) != (3, 0) and (I, J) != (3, 2):
                        ret += self.dfs(I, J, r - 1)
                        ret %= MOD

            self.cache[i, j, r] = ret

        return self.cache[i, j, r]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""n""i""g""h""t""D""i""a""l""e""r""(""1"")"" ""=""="" ""1""0""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""n""i""g""h""t""D""i""a""l""e""r""(""2"")"" ""=""="" ""2""0""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""n""i""g""h""t""D""i""a""l""e""r""(""3"")"" ""=""="" ""4""6""
