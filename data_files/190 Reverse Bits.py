
__author__ = 'Daniel'


class Solution:
    def reverseBits(self, n):
        
        ret = 0
        BITS = 32
        for i in xrange(BITS):
            ret += n&1
            if i == BITS-1: break
            ret <<= 1
            n >>= 1

        return ret
