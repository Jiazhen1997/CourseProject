

__author__ = 'Daniel'


class Solution(object):
    def getSum(self, a, b):
        
        MAX = 0x7FFFFFFF
        MSK = 0xFFFFFFFF

        carry = (a & b) << 1
        out = a ^ b

        
        carry &= MSK
        out &= MSK

        if carry != 0:
            return self.getSum(out, carry)
        else:
            
            if out < MAX:
                return out
            else:  
                return ~(out ^ MSK)