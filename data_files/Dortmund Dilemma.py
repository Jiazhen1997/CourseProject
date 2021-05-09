
__author__ = 'Danyang'
MOD = 10 ** 9 + 9


class Solution(object):
    def __init__(self):
        self.factorials = [0 for _ in xrange(26 + 1)]
        self.factorials[0] = 1
        for i in xrange(1, 26 + 1):
            self.factorials[i] = self.factorials[i - 1] * i


        
        N = 10 ** 5
        K = 26

        self.F = [[0 for _ in xrange(K + 1)] for _ in xrange(N + 1)]
        
        for j in xrange(1, K + 1):
            self.F[1][j] = j
            for i in xrange(2, N + 1):
                if i & 1 == 0:
                    self.F[i][j] = (self.F[i - 1][j] * j - self.F[i / 2][j])
                else:
                    self.F[i][j] = (self.F[i - 1][j] * j)
                self.F[i][j] %= MOD

        self.G = [[0 for _ in xrange(K + 1)] for _ in xrange(N + 1)]

        for j in xrange(1, K + 1):
            total = j
            for i in xrange(1, N + 1):
                self.G[i][j] = total - self.F[i][j]  
                self.G[i][j] %= MOD

                total *= j
                total %= MOD  

    def solve(self, cipher):
        
        N, K = cipher

        P = 0
        if K == 1:
            P += self.G[N][K]
        else:
            for j in xrange(K, 0, -1):
                
                
                
                P += (-1) ** (K - j) * self.G[N][j] * (
                    self.factorials[K] / (self.factorials[j] * self.factorials[K - j]))
                P %= MOD

        result = P * (self.factorials[26] / (self.factorials[K] * self.factorials[26 - K]))
        return result % MOD


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(