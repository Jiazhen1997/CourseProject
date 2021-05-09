
__author__ = 'Danyang'


class Queue:
    def __init__(self):
        
        self.in_stk = []
        self.out_stk = []

    def push(self, element):
        self.in_stk.append(element)

    def top(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        return self.out_stk[-1]

    def pop(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())

        return self.out_stk.pop()

