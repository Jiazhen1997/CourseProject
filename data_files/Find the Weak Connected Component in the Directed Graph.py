


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return repr(self.x)

from collections import defaultdict
__author__ = 'Daniel'


class UnionFind(object):
    
    def __init__(self):
        self.pi = {}  
        self.sz = {}  

    def add(self, item):
        if item not in self.pi:
            self.pi[item] = item
            self.sz[item] = 1

    def union(self, a, b):
        pi1 = self._pi(a)
        pi2 = self._pi(b)

        if pi1 != pi2:
            if self.sz[pi1] > self.sz[pi2]:
                pi1, pi2 = pi2, pi1

            self.pi[pi1] = pi2
            self.sz[pi2] += self.sz[pi1]
            del self.sz[pi1]

    def _pi(self, item):
        pi = self.pi[item]
        if item != pi:
            self.pi[item] = self._pi(pi)

        return self.pi[item]

    def compress(self):
        for item in self.pi.keys():
            self.pi[item] = self._pi(item)

    def count(self):
        return len(self.sz)  


class Solution:
    def connectedSet2(self, nodes):
        
        uf = UnionFind()
        for node in nodes:
            uf.add(node.label)
            for nei in node.neighbors:
                uf.add(nei.label)
                uf.union(node.label, nei.label)

        uf.compress()
        ret = defaultdict(list)
        for item, pi in uf.pi.items():
            ret[pi].append(item)

        for v in ret.values():
            v.sort()

        return ret.values()

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""t""e""m""s"" ""="" ""{""i"":"" ""D""i""r""e""c""t""e""d""G""r""a""p""h""N""o""d""e""(""i"")"" ""f""o""r"" ""i"" ""i""n"" 