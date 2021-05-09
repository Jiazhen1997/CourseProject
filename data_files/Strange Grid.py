

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        r, c = cipher
        r, c = r - 1, c - 1

        return r / 2 * 10 + r % 2 + c * 2


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(