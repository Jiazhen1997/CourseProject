
__author__ = 'Daniel'


class Solution:
    def rangeBitwiseAnd(self, m, n):
        
        pos = 0
        while m != n:
            pos += 1
            m >>= 1
            n >>= 1

        return n << pos  

