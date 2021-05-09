



class MyCircularQueue:

    def __init__(self, k: int):
        
        self.head = 0
        self.tail = -1
        self.sz = 0
        self.k = k
        self.lst = [None for _ in range(k)]


    def enQueue(self, value: int) -> bool:
        
        if self.sz >= self.k:
            return False

        self.tail += 1
        self.lst[self.tail % self.k] = value
        self.sz += 1
        return True

    def deQueue(self) -> bool:
        
        if self.sz <= 0:
            return False

        self.lst[self.head % self.k] = None
        self.head += 1
        self.sz -= 1
        return True

    def Front(self) -> int:
        
        ret = self.lst[self.head % self.k]
        return ret if ret is not None else -1

    def Rear(self) -> int:
        
        ret = self.lst[self.tail % self.k]
        return ret if ret is not None else -1

    def isEmpty(self) -> bool:
        
        return self.sz == 0

    def isFull(self) -> bool:
        
        return self.sz == self.k










