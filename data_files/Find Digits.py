
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        num = int(cipher)
        cnt = 0
        for char in cipher:
            digit = int(char)
            if digit == 0: continue
            if num % digit == 0:
                cnt += 1

        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(