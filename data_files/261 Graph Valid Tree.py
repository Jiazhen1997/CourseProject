
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def validTree(self, n, edges):
        
        if not edges:
            return n in (0, 1)

        V = defaultdict(list)
        for e in edges:
            V[e[0]].append(e[1])
            V[e[1]].append(e[0])

        visited = set()
        pathset = set()
        if not self.dfs(V, edges[0][0], None, pathset, visited):
            return False

        return len(visited) == n

    def dfs(self, V, v, pi, pathset, visited):
        if v in pathset:
            return False

        pathset.add(v)
        for nbr in V[v]:
            if nbr != pi:  
                if not self.dfs(V, nbr, v, pathset, visited):
                    return False

        pathset.remove(v)
        visited.add(v)
        return True