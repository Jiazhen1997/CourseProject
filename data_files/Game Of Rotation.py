
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = cipher
        N = len(A)
        _sum = sum(A)
        _max = -1 << 65  

        s = 0
        for ind, val in enumerate(A):
            s += (ind + 1) * val

        _max = max(_max, s)
        for i in xrange(N):
            s = s + _sum - N * A[N - 1 - i]
            _max = max(_max, s)

        return _max


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(