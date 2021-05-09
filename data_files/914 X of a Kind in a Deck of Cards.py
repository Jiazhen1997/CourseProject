

from typing import List
from collections import Counter


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        counter = Counter(deck)
        gcd = None
        for v in counter.values():
            if gcd is None:
                gcd = v
            gcd = self.gcd(gcd, v)
            if gcd == 1:
                return False

        return True

    def gcd(self, a, b):
        
        while b:
            a, b = b, a % b

        return a
