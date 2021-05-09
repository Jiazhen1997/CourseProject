
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, lst = cipher
        for i in xrange(N):
            for j in xrange(i + 1, N):
                if self.gcd(lst[i], lst[j]) == 1:
                    return "Y"E"S""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 