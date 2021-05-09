

import heapq

__author__ = 'Daniel'


class DualHeap(object):
    def __init__(self):
        
        self.min_h = []
        self.max_h = []

    def insert(self, num):
        if not self.min_h or num > self.min_h[0]:
            heapq.heappush(self.min_h, num)
        else:
            heapq.heappush(self.max_h, -num)
        self.balance()

    def balance(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        if abs(l1 - l2) <= 1:
            return
        elif l1 - l2 > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            self.balance()
        else:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
            self.balance()

    def get_median(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        if (l1 + l2) % 2 == 1:
            m = (l1 + l2) / 2  
            if m < l2:
                return -self.max_h[0]
            else:
                return self.min_h[0]
        else:
            return (-self.max_h[0] + self.min_h[0]) / 2.0


class MedianFinder(object):
    def __init__(self):
        
        self.dh = DualHeap()

    def addNum(self, num):
        
        self.dh.insert(num)

    def findMedian(self):
        
        return self.dh.get_median()
