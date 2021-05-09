

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        m = len(cipher)
        n = len(cipher[0])
        cipher = map(lambda x: sorted(x), cipher)
        
        for j in xrange(n):
            for i in xrange(m - 1):
                if cipher[i][j] > cipher[i + 1][j]:
                    return "N"O""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 