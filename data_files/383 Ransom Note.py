
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        d = defaultdict(int)

        for e in magazine:
            d[e] += 1

        for e in ransomNote:
            if d[e] == 0:
                return False
            d[e] -= 1

        return True