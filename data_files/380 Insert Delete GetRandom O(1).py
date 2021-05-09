
import random

__author__ = 'Daniel'


class RandomizedSet(object):
    def __init__(self):
        
        self.lst = []
        self.pos = {}

    def insert(self, val):
        
        if val in self.pos:
            return False

        self.lst.append(val)
        self.pos[val] = len(self.lst) - 1

        return True

    def remove(self, val):
        
        if val not in self.pos:
            return False

        idx, last = self.pos[val], len(self.lst) - 1

        if idx != last:
            self.lst[idx], self.lst[last] = self.lst[last], self.lst[idx]
            self.pos[self.lst[idx]] = idx

        del self.pos[val]
        self.lst.pop()

        return True

    def getRandom(self):
        
        return random.choice(self.lst)


class RandomizedSetTLE(object):
    def __init__(self):
        
        self.set = set()

    def insert(self, val):
        
        ret = val not in self.set
        self.set.add(val)
        return ret

    def remove(self, val):
        
        ret = val in self.set
        self.set.discard(val)
        return ret

    def getRandom(self):
        
        return random.sample(self.set, 1)[0]  








