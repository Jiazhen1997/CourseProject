

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        B = cipher
        N = len(B)
        dp = [[0, 0] for _ in xrange(N + 1)]

        LOW = 0
        HIGH = 1
        for i in xrange(2, N + 1):
            dp[i][LOW] = max(dp[i - 1][LOW], dp[i - 1][HIGH] + abs(1 - B[i - 2]))
            dp[i][HIGH] = max(dp[i - 1][HIGH], dp[i - 1][LOW] + abs(B[i - 1] - 1))

        return str(max(dp[-1][LOW], dp[-1][HIGH]))


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(