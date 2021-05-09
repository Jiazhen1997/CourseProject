
import random

__author__ = 'Daniel'


class Solution(object):
    def __init__(self, nums):
        
        self.A = nums

    def pick(self, target):
        
        sz = 0
        ret = None
        for idx, val in enumerate(self.A):
            if val == target:
                sz += 1
                p = random.randrange(0, sz)
                if p == 0:
                    ret = idx

        return ret


class SolutionError(object):
    def __init__(self, nums):
        
        self.d = {}
        for idx, val in enumerate(nums):
            if val not in self.d:
                self.d[val] = (idx, 1)
            else:
                prev, sz = self.d[val]
                p = random.randrange(0, sz)
                if p < sz:
                    self.d[val] = (idx, sz + 1)
                else:
                    self.d[val] = (prev, sz + 1)

    def pick(self, target):
        
        return self.d[target][0]