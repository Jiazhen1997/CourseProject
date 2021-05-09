
__author__ = 'Danyang'
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    def topSort_error(self, graph):
        
        node2neighbors = {}
        for node in graph:
            node2neighbors[node] = set(node.neighbors)

        
        def cmp(a, b):
            if a in node2neighbors[b]:
                return 1
            if b in node2neighbors[a]:
                return -1
            return 0

        graph.sort(cmp=cmp)
        return graph

    def topSort_normal(self, graph):
        
        pi = {}
        for node in graph:
            pi[node] = set()

        for node in graph:
            for nbr in node.neighbors:
                pi[nbr].add(node)

        ret = []
        while graph:
            i = 0
            while i<len(graph):
                if len(pi[graph[i]])!=0:
                    i += 1
                else:
                    ret.append(graph[i])
                    for nbr in graph[i].neighbors:
                        if graph[i] in pi[nbr]:
                            pi[nbr].remove(graph[i])
                    graph.pop(i)
                    
                    
        return ret


    def topSort(self, graph):
        
        unvisited = set(graph)

        ret = []
        while unvisited:
            cur = unvisited.copy().pop()
            self.dfs(cur, unvisited, ret)

        return ret

    def dfs(self, cur, unvisited, ret):
        
        for nbr in cur.neighbors:
            if nbr in unvisited:
                self.dfs(nbr, unvisited, ret)
        ret.push(0, cur)  
        unvisited.remove(cur)
