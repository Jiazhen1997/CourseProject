
from collections import deque

__author__ = 'Daniel'


class HitCounter(object):
    def __init__(self):
        
        self.q = deque()

    def hit(self, timestamp):
        
        self.pop(timestamp)
        self.q.append(timestamp)

    def getHits(self, timestamp):
        
        self.pop(timestamp)
        return len(self.q)

    def pop(self, timestamp):
        while self.q and timestamp - self.q[0] >= 300:
            self.q.popleft()





