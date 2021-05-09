
__author__ = 'Daniel'


class Solution:
    def trailingZeroes(self, n):
        
        cnt = 0
        while n:
            n /= 5
            cnt += n

        return cnt
