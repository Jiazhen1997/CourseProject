

from typing import Callable
from threading import Semaphore

from collections import deque

class H2O:
    def __init__(self):
        self.hq = deque()
        self.oq = deque()

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.hq.append(releaseHydrogen)
        self.try_output()

    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.oq.append(releaseOxygen)
        self.try_output()

    def try_output(self):
        if len(self.hq) >= 2 and len(self.oq) >= 1:
            self.hq.popleft()()
            self.hq.popleft()()
            self.oq.popleft()()


class H2O_TLE2:
    def __init__(self):
        
        self.gates = [Semaphore(2), Semaphore(0)]  

    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.gates[0].acquire()
        
        releaseHydrogen()
        if self.gates[0].acquire(blocking=False):  
            
            self.gates[0].release()
        else:
            self.gates[1].release()


    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.gates[1].acquire()
        
        releaseOxygen()
        self.gates[0].release()
        self.gates[0].release()


class H2O_TLE:
    def __init__(self):
        
        self.h_cnt = 0
        self.locks = [Lock() for _ in range(3)]
        self.locks[1].acquire()


    def hydrogen(self, releaseHydrogen: Callable[[], None]) -> None:
        self.locks[0].acquire()
        self.h_cnt += 1
        
        releaseHydrogen()
        if self.h_cnt < 2:
            self.locks[0].release()
        else:
            self.locks[1].release()


    def oxygen(self, releaseOxygen: Callable[[], None]) -> None:
        self.locks[1].acquire()
        
        releaseOxygen()
        self.h_cnt = 0
        self.locks[0].release()
