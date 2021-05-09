
__author__ = 'Daniel'


class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        
        self.released = set()
        self.l = maxNumbers
        self.i = 0

    def get(self):
        
        if self.released:
            return self.released.pop()
        if self.i < self.l:
            ret = self.i
            self.i += 1
            return ret

        return -1

    def check(self, number):
        
        return number in self.released or self.i <= number < self.l

    def release(self, number):
        
        if self.i <= number < self.l:
            return

        self.released.add(number)






