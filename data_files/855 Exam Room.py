

import bisect


class ExamRoom:
    def __init__(self, N: int):
        
        self.N = N
        self.idxes = []  

    def seat(self) -> int:
        
        if not self.idxes:
            ret_idx = 0
        else:
            max_dist, ret_idx = 0, 0
            
            dist = self.idxes[0] - 0
            if dist > max_dist:
                max_dist = dist
                ret_idx = 0
            
            for j in range(len(self.idxes)-1):
                i = (self.idxes[j] + self.idxes[j+1]) // 2
                dist = min(abs(self.idxes[j] - i), abs(self.idxes[j+1] - i))
                if dist > max_dist:
                    max_dist = dist
                    ret_idx = i
            
            dist = self.N-1 - self.idxes[-1]
            if dist > max_dist:
                max_dist = dist
                ret_idx = self.N-1

        bisect.insort(self.idxes, ret_idx)
        return ret_idx

    def leave(self, p: int) -> None:
        self.idxes.remove(p)






