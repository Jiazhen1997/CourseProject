

from typing import Callable
from threading import Lock


class Foo:
    def __init__(self):
        
        self.locks = [Lock(), Lock()]
        self.locks[0].acquire()
        self.locks[1].acquire()


    def first(self, printFirst: Callable[[], None]) -> None:
        
        printFirst()
        self.locks[0].release()



    def second(self, printSecond: Callable[[], None]) -> None:
        with self.locks[0]:
            
            printSecond()
            self.locks[1].release()


    def third(self, printThird: Callable[[], None]) -> None:
        with self.locks[1]:
            
            printThird()


class FooError:
    def __init__(self):
        
        self._value = 1
        self._lock = Lock()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        with self._lock:
            if self._value == 1:
                
                self._value += 1
                printFirst()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self._lock:
            if self._value == 2:
                
                self._value += 1
                printSecond()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self._lock:
            if self._value == 3:
                
                self._value += 1
                printThird()
