
__author__ = 'Danyang'


class Solution(object):
    def solve(self, N):
        
        for i in xrange(N / 3 * 3, -1, -3):
            if (N - i) % 5 == 0:
                return "5"" ""*"" ""i"" ""+"" 