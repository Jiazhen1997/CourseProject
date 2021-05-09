

from typing import List
from collections import defaultdict
import bisect


class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        
        self.maxes = []  
        counter = defaultdict(int)
        tp = sorted(zip(times, persons))
        for t, p in tp:
            counter[p] += 1
            if not self.maxes or counter[self.maxes[-1][1]] <= counter[p]:
                self.maxes.append((t, p))

    def q(self, t: int) -> int:
        i = bisect.bisect(self.maxes, (t, 0))
        
        if i < len(self.maxes) and self.maxes[i][0] == t:
            return self.maxes[i][1]

        
        i -= 1
        return self.maxes[i][1]





