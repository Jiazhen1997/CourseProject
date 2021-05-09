
__author__ = 'Daniel'


class Logger(object):
    def __init__(self):
        
        self.h = {}


    def shouldPrintMessage(self, timestamp, message):
        
        if message not in self.h or timestamp - self.h[message] >= 10:
            self.h[message] = timestamp
            return True

        return False




