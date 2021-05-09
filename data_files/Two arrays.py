
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, K, A, B = cipher
        A.sort()
        B.sort(reverse=True)  
        for i in xrange(N):
            if not A[i] + B[i] >= K:
                return "N"O""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 