
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        return len(reduce(lambda x, y: x & y, [set(list(elt)) for elt in cipher]))


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(