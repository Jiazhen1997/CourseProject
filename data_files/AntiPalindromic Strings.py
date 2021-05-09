

__author__ = 'Danyang'

MOD = 10 ** 9 + 7


class Solution(object):
    def solve(self, cipher):
        
        N, M = cipher
        s = M
        if N > 1:
            s *= (M - 1)
        if N > 2:
            s *= pow(M - 2, N - 2, MOD)  
            s %= MOD
        return s % MOD

    def _exp(self, a, b):
        
        ret = 1
        b %= MOD
        while b > 0:
            if b & 1 == 0:
                b /= 2
                a *= a
                a %= MOD
            else:
                ret *= a
                ret %= MOD
                b -= 1
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(