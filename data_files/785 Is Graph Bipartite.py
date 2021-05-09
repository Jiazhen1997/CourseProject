

from collections import defaultdict


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        G = graph
        color = defaultdict(int)
        for k in range(len(G)):
            if k not in color:
                color[k] = 0
                if not self.dfs(G, k, color):
                    return False
            

        return True

    def dfs(self, G, u, color):
        for nbr in G[u]:
            if nbr in color:
                if color[nbr] == color[u]:
                    return False
            else:
                color[nbr] = 1 - color[u]  
                if not self.dfs(G, nbr, color):
                    return False

        return True


class SolutionError:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        G = graph
        A, B = set(), set()
        visited = defaultdict(bool)
        for k in range(len(G)):
            if not visited[k]:
                if not self.dfs(G, visited, k, A, B, True):
                    return False

        return True

    def dfs(self, G, visited, u, A, B, is_A):
        visited[u] = True
        if is_A:
            A.add(u)
        else:
            B.add(u)

        for nbr in G[u]:
            if nbr in A if is_A else B:
                return False
            if not visited[nbr]:
                if not self.dfs(G, visited, nbr, A, B, False):
                    return False

        return True
