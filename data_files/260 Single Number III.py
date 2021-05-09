
__author__ = 'Daniel'


class Solution:
    def singleNumber(self, nums):
        
        bits = 0
        for elt in nums:
            bits ^= elt

        rightmost_bit_set = bits & -bits
        a = 0
        b = 0
        for elt in nums:
            if elt & rightmost_bit_set:
                a ^= elt
            else:
                b ^= elt

        return a, b