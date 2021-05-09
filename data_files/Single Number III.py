
__author__ = 'Danyang'


class Solution:
    def singleNumberIII(self, A):
        
        bits = 0
        for a in A:
            bits ^= a

        rightmost_set_bit = bits&-bits

        bits1 = 0
        bits2 = 0
        for a in A:
            if a&rightmost_set_bit:
                bits1 ^= a
            else:
                bits2 ^= a

        return bits1, bits2


