

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K = cipher
        if K < N / 2:
            return 2 * K + 1
        else:
            return 2 * (N - 1 - K)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(