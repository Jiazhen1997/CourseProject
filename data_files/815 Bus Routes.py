

from typing import List
from collections import defaultdict


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        
        if S == T:
            return 0

        routes = [set(e) for e in routes]
        G = defaultdict(set)
        for i in range(len(routes)):
            for j in range(i + 1, len(routes)):
                stops_1, stops_2 = routes[i], routes[j]  
                for stop in stops_1:  
                    if stop in stops_2:
                        G[i].add(j)
                        G[j].add(i)
                        break

        q = [i for i, stops in enumerate(routes) if S in stops]
        target_set = set([i for i, stops in enumerate(routes) if T in stops])
        visited = defaultdict(bool)
        for i in q:
            visited[i] = True
        step = 1
        while q:
            cur_q = []
            for e in q:
                if e in target_set:
                    return step
                for nbr in G[e]:
                    if not visited[nbr]:
                        visited[nbr] = True
                        cur_q.append(nbr)

            step += 1
            q = cur_q

        return -1

    def numBusesToDestination_TLE(self, routes: List[List[int]], S: int, T: int) -> int:
        
        G = defaultdict(set)
        for stops in routes:
            for i in range(len(stops)):
                for j in range(i + 1, len(stops)):
                    u, v = stops[i], stops[j]
                    G[u].add(v)
                    G[v].add(u)

        q = [S]
        step = 0
        visited = defaultdict(bool)
        visited[S] = True  
        while q:
            cur_q = []
            for e in q:
                if e == T:
                    return step
                for nbr in G[e]:
                    if not visited[nbr]:
                        visited[nbr] = True
                        cur_q.append(nbr)

            step += 1
            q = cur_q

        return -1


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""B""u""s""e""s""T""o""D""e""s""t""i""n""a""t""i""o""n""(""[""[""1"","" ""2"","" ""7""]"","" ""[""3"","" ""6"","" ""7""]""]"","" ""1"","" ""6"")"" ""=""="" ""2""
