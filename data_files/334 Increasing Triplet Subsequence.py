
import sys

__author__ = 'Daniel'


class Solution(object):
    def increasingTriplet(self, nums):
        
        min1 = sys.maxint
        min2 = sys.maxint
        for e in nums:
            if e < min1:
                min1 = e
            elif e != min1 and e < min2:
                min2 = e
            elif e > min2:
                return True

        return False

    def increasingTripletError(self, nums):
        
        stk = []
        for elt in nums:
            while stk and stk[-1] >= elt:
                stk.pop()

            stk.append(elt)
            if len(stk) >= 3:
                return True

        return False
