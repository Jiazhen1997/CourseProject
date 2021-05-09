

from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        
        capital_q = list(zip(Capital, Profits))
        profit_q = []
        heapq.heapify(capital_q)
        capital = W
        for _ in range(k):
            while capital_q and capital_q[0][0] <= capital:
                _, pro = heapq.heappop(capital_q)
                heapq.heappush(profit_q, (-pro, pro))

            if profit_q:
                _, pro = heapq.heappop(profit_q)
                capital += pro
            else:
                break

        return capital

    def findMaximizedCapital_TLE(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        
        capital = W
        n = len(Profits)
        visited = [False for _ in range(n)]
        for _ in range(k):
            maxa = 0
            maxa_i = 0
            for i in range(n):
                if not visited[i] and Profits[i] >= maxa and Capital[i] <= capital:
                    maxa = Profits[i]
                    maxa_i = i
            if maxa > 0:
                capital += maxa
                visited[maxa_i] = True
            else:
                break

        return capital
