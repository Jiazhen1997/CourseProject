
import heapq
from collections import defaultdict, deque

__author__ = 'Daniel'


class Solution(object):
    def findItinerary(self, tickets):
        
        G = defaultdict(list)  
        for s, e in tickets:
            heapq.heappush(G[s], e)  

        ret = deque()
        self.dfs(G, 'JFK', ret)
        return list(ret)

    def dfs(self, G, cur, ret):
        while G[cur]:
            self.dfs(G, heapq.heappop(G[cur]), ret)

        ret.appendleft(cur)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""I""t""i""n""e""r""a""r""y""(""[""[