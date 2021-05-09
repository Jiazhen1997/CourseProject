

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        f = [0 for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            f[i] = f[i - 1] + A[i - 1]

        for i in xrange(N):
            if f[i] == f[N] - f[i + 1]:
                return "Y"E"S""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 