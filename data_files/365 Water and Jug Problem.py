
__author__ = 'Daniel'


class Solution(object):
    def canMeasureWater(self, x, y, z):
        
        if x + y < z: return False
        if x == z or y == z: return True

        return z % self.gcd(x, y) == 0

    def gcd(self, a, b):
        while b:
            a, b = b, a%b
        return a

