
from collections import deque

__author__ = 'Daniel'


class MovingAverage(object):
    def __init__(self, size):
        
        self.size = size
        self.q = deque()
        self.sum = 0

    def next(self, val):
        
        self.q.append(val)
        self.sum += val
        if len(self.q) > self.size:
            self.sum -= self.q.popleft()

        return float(self.sum) / len(self.q)




