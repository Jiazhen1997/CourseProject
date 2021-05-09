


__author__ = 'Daniel'


class Solution(object):
    def isPowerOfFour(self, num):
        
        if num < 1:
            return False
        if num & num -1 != 0:
            return False

        return num % 3 == 1

    def isPowerOfFourNaive(self, num):
        
        if num < 1:
            return False
        if num & num-1 != 0:
            return False

        while True:
            if num == 0:
                return False
            elif num == 1:
                return True

            num >>= 2