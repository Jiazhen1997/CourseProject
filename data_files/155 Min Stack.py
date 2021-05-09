
__author__ = 'Danyang'


class MinStack:
    def __init__(self):
        
        self.stk = []
        self.non_asc = []

    def push(self, x):
        
        self.stk.append(x)
        if len(self.non_asc) == 0 or x <= self.non_asc[-1]:  
            self.non_asc.append(x)

    def pop(self):
        
        x = self.stk.pop()
        if x == self.non_asc[-1]:
            self.non_asc.pop()

    def top(self):
        
        return self.stk[-1]

    def getMin(self):
        
        return self.non_asc[-1]

