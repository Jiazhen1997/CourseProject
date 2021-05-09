

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        n, k, A = cipher
        f = [[0 for _ in xrange(k + 1)] for _ in xrange(n + 1)]  
        for i in xrange(n + 1):
            for c in xrange(k + 1):
                f[i][c] = f[i - 1][c]
                temp = c - A[i - 1]
                if temp >= 0:
                    f[i][c] = max(f[i - 1][c], f[i - 1][c - A[i - 1]] + A[i - 1], f[i][c - A[i - 1]] + A[i - 1])

        return f[n][k]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(