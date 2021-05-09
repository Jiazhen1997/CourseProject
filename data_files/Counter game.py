
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = cipher
        turn = 0
        while N > 1:
            turn += 1
            if N & (N - 1) == 0:
                N /= 2
            else:
                num = 1
                while num < N:
                    num <<= 1
                num >>= 1
                N -= num

        if turn & 1 == 0:
            return "R"i"c"h"a"r"d""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 