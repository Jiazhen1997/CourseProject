
__author__ = 'Daniel'


class Solution:
    def hammingWeight(self, n):
        
        cnt = 0
        while n:
            cnt += n&1
            n >>= 1

        return cnt
