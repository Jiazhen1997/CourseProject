
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A, B, N = cipher

        a, b = A, B
        cnt = 1
        while cnt < N:
            cnt += 1
            a, b = b, b * b + a

        return a


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(