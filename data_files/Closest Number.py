

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        a, b, x = cipher
        if a > 1:
            result = int((a ** b) / float(x) + 0.5) * x
        else:
            result = 1
        if result != int(result):
            if result > 0.5 and x == 1:
                return 1
            else:
                return 0
        return result


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(