
__author__ = 'Daniel'


class Iterator(object):
    def __init__(self, nums):
        

    def hasNext(self):
        

    def next(self):
        


class PeekingIterator(object):
    def __init__(self, iterator):
        
        self.nxt = None
        self.iterator = iterator

    def peek(self):
        
        if not self.nxt:
            self.nxt = self.iterator.next()

        return self.nxt

    def next(self):
        
        ret = self.peek()
        self.nxt = None
        return ret

    def hasNext(self):
        
        return self.nxt is not None or self.iterator.hasNext()
