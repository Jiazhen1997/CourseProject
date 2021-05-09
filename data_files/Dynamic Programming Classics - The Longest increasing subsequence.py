
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        maxa = 1
        f = [1 for _ in xrange(N)]
        for i in xrange(1, N):
            for j in xrange(i):
                if A[i] > A[j]:
                    f[i] = max(f[i], f[j] + 1)
            maxa = max(maxa, f[i])
        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(