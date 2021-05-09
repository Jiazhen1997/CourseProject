

from typing import Callable
from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        
        self.n = n
        self.locks = [Lock() for _ in range(3)]
        self.locks[1].acquire()
        self.locks[2].acquire()

	
    def zero(self, printNumber: Callable[[int], None]) -> None:
        for i in range(self.n):
            self.locks[0].acquire()
            printNumber(0)
            if (i + 1) % 2 == 1:
                self.locks[1].release()
            else:
                self.locks[2].release()

    def odd(self, printNumber: Callable[[int], None]) -> None:
        for i in range((self.n + 1) // 2):
            self.locks[1].acquire()
            printNumber(i * 2 + 1)
            self.locks[0].release()

    def even(self, printNumber: Callable[[int], None]) -> None:
        for i in range(self.n // 2):
            self.locks[2].acquire()
            printNumber(i * 2 + 2)
            self.locks[0].release()


class ZeroEvenOddError:
    def __init__(self, n):
        
        self.n = n
        self.locks = [Lock(), Lock(), Lock(), Lock()]
        for i in range(1, len(self.locks)):
            self.locks[i].acquire()

	
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        with self.locks[0]:
            printNumber(0)

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        
        pass


    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        pass
