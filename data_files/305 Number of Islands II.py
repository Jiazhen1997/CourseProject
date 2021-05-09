
from collections import namedtuple

__author__ = 'Daniel'


class UnionFind(object):
    
    def __init__(self, rows, cols):
        
        self.pi = [-1 for _ in xrange(rows*cols)]  
        self.sz = [-1 for _ in xrange(rows*cols)]  
        self.count = 0

    def add(self, item):
        if self.pi[item] == -1:
            self.pi[item] = item
            self.sz[item] = 1
            self.count += 1

    def union(self, a, b):
        pi1 = self._pi(a)
        pi2 = self._pi(b)

        if pi1 != pi2:
            if self.sz[pi1] > self.sz[pi2]:
                pi1, pi2 = pi2, pi1

            self.pi[pi1] = pi2
            self.sz[pi2] += self.sz[pi1]
            self.count -= 1

    def _pi(self, item):
        
        pi = self.pi[item]
        if item != pi:
            self.pi[item] = self._pi(pi)

        return self.pi[item]


Op = namedtuple('Op', 'r c')  


class Solution:
    def __init__(self):
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def numIslands2(self, n, m, operators):
        rows = n
        cols = m
        unroll = lambda x, y: x*cols + y  
        mat = [[0 for _ in xrange(cols)] for _ in xrange(rows)]
        uf = UnionFind(rows, cols)
        ret = []
        for op in operators:
            op = Op(r=op[0], c=op[1])
            uf.add(unroll(op.r, op.c))
            mat[op.r][op.c] = 1
            for dir in self.dirs:
                x1 = op.r+dir[0]
                y1 = op.c+dir[1]
                if 0 <= x1 < rows and 0 <= y1 < cols and mat[x1][y1] == 1:
                    uf.union(unroll(op.r, op.c), unroll(x1, y1))

            ret.append(uf.count)

        return ret