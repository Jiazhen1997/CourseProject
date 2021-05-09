

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        f = [0 for _ in A]
        f[N - 1] = A[N - 1]
        for i in xrange(N - 2, -1, -1):
            f[i] = max(A[i], f[i + 1])

        profit = 0
        for i in xrange(N - 1):
            profit += max(0, f[i + 1] - A[i])

        return profit


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(