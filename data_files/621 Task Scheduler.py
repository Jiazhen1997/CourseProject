

from typing import List
from collections import deque, defaultdict
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1

        maxa = 0
        max_cnt = 0
        for v in counter.values():
            if v > maxa:
                maxa = v
                max_cnt = 1
            elif v == maxa:
                max_cnt += 1

        page_cnt = maxa - 1
        free_page_size = n + 1 - max_cnt
        small_tasks = len(tasks) - max_cnt * maxa
        idle = max(0, page_cnt * free_page_size - small_tasks)
        return len(tasks) + idle


    def leastInterval_complicated(self, tasks: List[str], n: int) -> int:
        
        counter = defaultdict(int)
        for t in tasks:
            counter[t] += 1

        pq = [
            (-v, k)
            for k, v in counter.items()
        ]
        heapq.heapify(pq)
        q = deque()  
        clock = 0
        while pq or q:
            if q and q[0][0] <= clock:
                
                _, k = q.popleft()
                heapq.heappush(pq, (-counter[k], k))

            if pq:
                _, k = heapq.heappop(pq)
                counter[k] -= 1
                if counter[k] > 0:
                    q.append((clock + 1 + n, k))

            clock += 1

        return clock


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""a""s""t""I""n""t""e""r""v""a""l""(""[