

from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        G = defaultdict(dict)
        visited = defaultdict(bool)
        for u, v, w in flights:
            G[u][v] = w

        pq = [(0, 0, src)]  
        while pq:
            cost, k, u = heapq.heappop(pq)
            if u == dst:
                return cost

            stops = k - 1 + 1
            if stops <= K:
                for v, w in G[u].items():
                    heapq.heappush(pq, (cost + w, k + 1, v))


        return -1
