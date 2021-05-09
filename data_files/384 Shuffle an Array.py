
import random

__author__ = 'Daniel'


class Solution(object):
    def __init__(self, nums):
        
        self.original = nums

    def reset(self):
        
        return list(self.original)

    def shuffle(self):
        
        lst = self.reset()
        n = len(lst)
        for i in xrange(n):
            j = random.randrange(i, n)
            lst[i], lst[j] = lst[j], lst[i]

        return lst





