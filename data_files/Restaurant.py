

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        l, b = cipher
        r = self.gcd(l, b)
        return (l * b) / (r * r)

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(