

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = sorted(cipher)
        cur = -5
        cnt = 0
        for a in A:
            if cur + 4 < a:
                cur = a
                cnt += 1
        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(