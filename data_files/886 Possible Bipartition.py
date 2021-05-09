

from typing import List
from collections import defaultdict


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        
        G = defaultdict(list)
        for u, v in dislikes:
            G[u].append(v)
            G[v].append(u)

        visited = {}  
        for u in range(1, N+1):
            if u not in visited:
                if not self.dfs(u, G, visited, 0):
                    return False
        return True

    def dfs(self, u, G, visited, color):
        visited[u] = color
        for nbr in G[u]:
            if nbr in visited:
                if visited[nbr] == color:
                    return False
            else:
                if not self.dfs(nbr, G, visited, color ^ 1):
                    return False

        return True
