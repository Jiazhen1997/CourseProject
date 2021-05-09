
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        ret = 0
        for i, val in enumerate(A):
            if (i + 1) * (N - i) % 2 == 1:
                ret ^= val
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(