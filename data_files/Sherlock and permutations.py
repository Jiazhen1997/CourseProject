
MOD = 10 ** 9 + 7
import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, M = cipher
        return math.factorial(N + M - 1) / math.factorial(N) / math.factorial(M - 1) % MOD


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(