
__author__ = 'Daniel'






def guess(num):
    return -1


class Solution(object):
    def guessNumber(self, n):
        
        lo, hi = 1, n+1
        while True:
            mid = (lo + hi) / 2
            g = guess(mid)
            if g == 0:
                return mid
            elif g < 1:
                hi = mid
            else:
                lo = mid + 1
