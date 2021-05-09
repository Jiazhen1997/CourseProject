
__author__ = 'Daniel'


class Stack:
    def __init__(self):
        
        self.q = [[], []]

    def push(self, x):
        
        t = 0
        if not self.q[t]:
            t ^= 1

        self.q[t].append(x)

    def pop(self):
        
        t = 0
        if not self.q[t]:
            t ^= 1

        while len(self.q[t]) > 1:
            self.q[t^1].append(self.q[t].pop(0))

        return self.q[t].pop()

    def top(self):
        
        popped = self.pop()
        t = 0
        if not self.q[t]:
            t ^= 1

        self.q[t].append(popped)
        return popped

    def empty(self):
        
        return not self.q[0] and not self.q[1]
