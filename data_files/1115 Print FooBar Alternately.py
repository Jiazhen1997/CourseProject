

from threading import Lock
from typing import Callable


class FooBar:
    def __init__(self, n):
        self.n = n
        self.locks = [Lock(), Lock()]
        self.locks[1].acquire()


    def foo(self, printFoo: Callable[[], None]) -> None:
        for i in range(self.n):
            self.locks[0].acquire()
            
            printFoo()
            self.locks[1].release()


    def bar(self, printBar: Callable[[], None]) -> None:
        for i in range(self.n):
            self.locks[1].acquire()
            
            printBar()
            self.locks[0].release()
