

import collections

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        d = collections.defaultdict(int)
        lst = list(cipher)
        n = len(lst)
        for i in xrange(n):
            for l in xrange(1, n - i + 1):
                sub = lst[i: i + l]
                sub.sort()
                d["".""j""o""i""n""(""s""u""b"")""]"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" ""s"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""v"" ""i""n"" ""d"".""v""a""l""u""e""s""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s"" ""+""="" ""v"" ""*"" ""(""v"" ""-"" ""1"")"" ""/"" ""2""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 