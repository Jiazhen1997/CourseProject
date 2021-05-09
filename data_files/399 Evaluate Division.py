
from collections import defaultdict
from itertools import izip

__author__ = 'Daniel'


class Solution(object):
    def calcEquation(self, equations, values, queries):
        
        G = defaultdict(dict)
        for edge, val in izip(equations, values):
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        return [self.dfs(G, s, e, set()) for s, e in queries]

    def dfs(self, G, s, e, path):
        if s not in G or e not in G:
            return -1.0
        if e in G[s]:
            return G[s][e]
        for nbr in G[s]:
            if nbr not in path:
                path.add(nbr)
                val = self.dfs(G, nbr, e, path)
                if val != -1.0:
                    return val * G[s][nbr]
                path.remove(nbr)

        return -1.0


class Solution(object):
    def calcEquation(self, equations, values, queries):
        
        G = defaultdict(dict)
        for edge, val in izip(equations, values):
            s, e = edge
            G[s][e], G[e][s] = val, 1/val
            G[s][s], G[e][e] = 1, 1

        
        for mid in G:
            for s in G[mid]:
                for e in G[mid]:
                    G[s][e] = G[s][mid] * G[mid][e]

        return [G[s].get(e, -1.0) for s, e in queries]

