

from typing import List


class RLEIterator:
    def __init__(self, A: List[int]):
        
        self.cur_i = 0
        self.cur_used = 0
        self.A = A

    def next(self, n: int) -> int:
        run = self.cur_used + n
        while self.cur_i < len(self.A) and run > self.A[self.cur_i]:
            run -= self.A[self.cur_i]
            self.cur_i += 2

        if self.cur_i >= len(self.A):
            return -1

        self.cur_used = run
        return self.A[self.cur_i + 1]
