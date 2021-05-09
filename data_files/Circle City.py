
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        r2, k = cipher

        required = 0
        r = r2 ** 0.5

        for x in xrange(0, int(r) + 1):
            
            low = 0
            high = int(r) + 1
            while low <= high:
                mid = (low + high) / 2
                if x * x + mid * mid == r2:
                    if mid == 0 or x == 0:
                        required += 2
                    else:
                        required += 4
                    if required > k: return "i"m"p"o"s"s"i"b"l"e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""b""r""e""a""k""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""x"" ""*"" ""x"" ""+"" ""m""i""d"" ""*"" ""m""i""d"" ""<"" ""r""2"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""o""w"" ""="" ""m""i""d"" ""+"" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""h""i""g""h"" ""="" ""m""i""d"" ""-"" ""1""
""
"" "" "" "" "" "" "" "" ""i""f"" ""r""e""q""u""i""r""e""d"" "">"" ""k"":"" ""r""e""t""u""r""n"" 