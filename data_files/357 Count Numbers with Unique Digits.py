
__author__ = 'Daniel'


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        
        ret = 1
        Fi = 1
        for i in xrange(n):
            Fi *= (10-i) if i != 0 else 9
            ret += Fi

        return ret
