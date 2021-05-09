
__author__ = 'Daniel'


class Solution(object):
    def integerReplacement(self, n):
        
        ret = 0
        while n != 1:
            ret += 1
            if n & 1 == 0:
                n >>= 1
            elif n == 0b11 or n >> 1 & 1 == 0:
                n -= 1
            else:
                n += 1

        return ret

    def integerReplacementRecur(self, n):
        
        if n == 1: return 0

        ret = 1
        if n%2 == 0:
            ret += self.integerReplacement(n/2)
        else:
            ret += min(self.integerReplacement(n+1), self.integerReplacement(n-1))

        return ret
