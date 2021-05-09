

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        G = defaultdict(dict)
        reach_time = [float('inf') for _ in range(N + 1)]
        for u, v, w in times:
            G[u][v] = w

        h = [(0, K)]
        reach_time[K] = 0
        while h:
            t, s = heapq.heappop(h)
            if s in G:
                for d, w in G[s].items():
                    if t + w < reach_time[d]:
                        reach_time[d] = t + w
                        heapq.heappush(h, (t + w, d))

        ret = max(reach_time[1:])  
        if ret == float('inf'):
            return -1
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""e""t""w""o""r""k""D""e""l""a""y""T""i""m""e""(""[""[""2"",""1"",""1""]"",""[""2"",""3"",""1""]"",""[""3"",""4"",""1""]""]"","" ""4"","" ""2"")"" ""=""="" ""2""
