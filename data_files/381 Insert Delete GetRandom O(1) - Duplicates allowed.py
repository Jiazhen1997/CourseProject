
from collections import defaultdict
import random

__author__ = 'Daniel'


class RandomizedCollection(object):
    def __init__(self):
        
        self.lst = []
        self.pos = defaultdict(set)

    def insert(self, val):
        
        flag = True if not self.pos[val] else False

        self.lst.append(val)
        self.pos[val].add(len(self.lst) - 1)

        return flag

    def remove(self, val):
        
        if not self.pos[val]:
            return False

        idx, last = self.pos[val].pop(), len(self.lst) - 1
        if idx != last:
            self.lst[idx], self.lst[last] = self.lst[last], self.lst[idx]
            self.pos[self.lst[idx]].remove(last)
            self.pos[self.lst[idx]].add(idx)

        self.lst.pop()

        return True

    def getRandom(self):
        
        return random.choice(self.lst)






