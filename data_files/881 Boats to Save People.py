

from typing import List
from collections import deque


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        ret = 0
        q = deque(sorted(people))
        while q:
            tail = q.pop()
            ret += 1
            if q and q[0] + tail <= limit:
                q.popleft()

        return ret
