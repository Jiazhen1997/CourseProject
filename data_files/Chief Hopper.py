

import math

__author__ = 'Danyang'


class Solution(object):
    def solve_error(self, cipher):
        
        N, H = cipher
        s = 0
        m = max(H)
        up = math.log(m, 2)
        for i, e in enumerate(H):
            if i > up and i > 1000:
                break
            s += float(e) / 2 ** (i + 1)
        return int(math.ceil(s))

    def solve(self, cipher):
        
        N, H = cipher
        mini = 0
        for i in xrange(N - 1, -1, -1):
            mini = (mini + H[i] + 1) / 2  
        return mini


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(