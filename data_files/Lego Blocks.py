

__author__ = 'Danyang'
MOD = 1000000007


class Solution(object):
    def __init__(self):
        self.lens = [1, 2, 3, 4]

    def solve(self, cipher):
        
        N, M = cipher
        f = [0 for _ in xrange(M + 1)]
        s = [0 for _ in xrange(M + 1)]

        f[0] = 1
        for j in xrange(1, M + 1):
            for l in self.lens:
                if j - l >= 0:
                    f[j] += f[j - l]
                f[j] %= MOD

        f_N = map(lambda x: pow(x, N, MOD), f)

        for j in xrange(1, M + 1):
            s[j] = f_N[j]
            if s[j] <= 0: break
            for k in xrange(1, j):  
                s[j] -= f_N[j - k] * s[k]
                s[j] %= MOD
        return s[M]


class Solution_TLE(object):
    def __init__(self):
        self.lens = [1, 2, 3, 4]

    def solve(self, cipher):
        
        N, M = cipher
        f = [[0 for _ in xrange(M + 1)] for _ in xrange(N + 1)]
        s = [[0 for _ in xrange(M + 1)] for _ in xrange(N + 1)]

        f[1][0] = 1
        for j in xrange(1, M + 1):
            for l in self.lens:
                if j - l >= 0:
                    f[1][j] += f[1][j - l]
                    f[1][j] %= MOD

        for i in xrange(2, N + 1):
            for j in xrange(1, M + 1):
                f[i][j] = f[i - 1][j] * f[1][j]
                f[i][j] %= MOD

        for i in xrange(1, N + 1):
            for j in xrange(1, M + 1):
                s[i][j] = f[i][j]
                if s[i][j] <= 0: break
                for k in xrange(1, j):  
                    s[i][j] -= f[i][j - k] * s[i][k]
                    s[i][j] %= MOD
        return s[N][M]

    def solve_error(self, cipher):
        
        N, M = cipher
        f = [[0 for _ in xrange(M + 1)] for _ in xrange(N + 1)]

        f[1][1] = 1
        for j in xrange(1, M + 1):
            for l in self.lens:
                if j - l >= 1:
                    f[1][j] += f[1][j - l]
        for j in xrange(1, M + 1):
            f[1][j] -= f[1][j - 1]

        for i in xrange(2, N + 1):
            for j in xrange(1, M + 1):
                cmb = i
                for l in xrange(1, i + 1):
                    f[i][j] += cmb * f[i - l][j - 1] * (f[1][j] ** i)  
                    cmb = cmb * (i - l) / (l + 1)
        return f[N][M]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(