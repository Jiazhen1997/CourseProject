

from typing import List
from collections import defaultdict


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        G = defaultdict(list)
        n = len(stones)
        for i in range(n):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    G[i].append(j)
                    G[j].append(i)

        
        comp_cnt = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                comp_cnt += 1
                self.dfs(G, i, visited)

        return n - comp_cnt

    def dfs(self, G, i, visited):
        visited[i] = True
        for nbr in G[i]:
            if not visited[nbr]:
                self.dfs(G, nbr, visited)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""r""e""m""o""v""e""S""t""o""n""e""s""(""[""[""0"",""0""]"",""[""0"",""2""]"",""[""1"",""1""]"",""[""2"",""0""]"",""[""2"",""2""]""]"")"" ""=""="" ""3""
