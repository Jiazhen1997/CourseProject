
__author__ = 'Daniel'


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def connectedSet(self, nodes):
        
        rets = []
        visisted = set()
        for node in nodes:
            if node not in visisted:
                ret = []
                self.dfs(node, visisted, ret)
                ret.sort()
                rets.append(ret)

        return rets

    def dfs(self, node, visited, ret):
        
        ret.append(node.label)
        visited.add(node)
        for nei in node.neighbors:
            if nei not in visited:
                self.dfs(nei, visited, ret)
