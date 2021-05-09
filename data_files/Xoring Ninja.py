
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        length, lst = cipher

        return reduce(lambda x, y: x | y, lst) * 2 ** (length - 1) % (10 ** 9 + 7)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(