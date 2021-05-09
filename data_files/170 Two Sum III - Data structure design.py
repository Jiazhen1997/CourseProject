
from collections import defaultdict

__author__ = 'Daniel'


class TwoSum(object):
    def __init__(self):
        
        self.hash_map = defaultdict(int)

    def add(self, number):
        
        self.hash_map[number] += 1

    def find(self, value):
        
        return any(
            value-k in self.hash_map and (value-k != k or self.hash_map[k] > 1)
            for k in self.hash_map
        )

    def find_TLE(self, value):
        
        for k in self.hash_map.keys():
            target = value - k
            if target in self.hash_map and (target != k or self.hash_map[target] > 1):
                return True

        return False
