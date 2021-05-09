
MOD = 10 ** 9
__author__ = 'Danyang'


class Solution(object):
    def __init__(self):
        
        self.C = [[1 for _ in xrange(2000)] for _ in xrange(2000)]
        for n in xrange(1, 2000):
            for k in xrange(1, n):  
                self.C[n][k] = self.C[n - 1][k - 1] + self.C[n - 1][k]

    def solve(self, cipher):
        
        N, K = cipher
        return self.C[N + K - 1][K] % MOD


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(