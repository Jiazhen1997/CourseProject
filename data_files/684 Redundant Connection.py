

from typing import List
from collections import defaultdict


class DisjointSet():
    def __init__(self):
        self.sz = {}  
        self.pi = {}  

    def add(self, x):
        if x not in self.pi:  
            self.sz[x] = 1
            self.pi[x] = x

    def unionize(self, x, y):
        p1 = self.root(x)
        p2 = self.root(y)
        if p1 != p2:
            sz1 = self.sz[p1]
            sz2 = self.sz[p2]
            if sz1 > sz2:
                p1, p2 = p2, p1

            self.pi[p1] = p2
            self.sz[p2] += self.sz[p1]
            del self.sz[p1]

    def root(self, x):
        p = self.pi[x]
        if p != x:
            self.pi[x] = self.root(p)

        return self.pi[x]

    def is_union(self, x, y):
        if x in self.pi and y in self.pi:
            return self.root(x) == self.root(y)

        return False


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        ds = DisjointSet()
        for p, q in edges:
            ds.add(p)
            ds.add(q)
            if ds.is_union(p, q):
                return [p, q]

            ds.unionize(p, q)

        raise

class Solution_dfs:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        G = defaultdict(set)
        for p, q in edges:
            G[p].add(q)
            G[q].add(p)

        visited = set()
        for k in G.keys():
            if k not in visited:
                circle = self.dfs(G, k, None, set([k]), [k], visited)
                if circle:
                    for p, q in reversed(edges):
                        if p in circle and q in circle:
                            return [p, q]

        raise

    def dfs(self, G, cur, pi, path, path_list, visited):
        visited.add(cur)

        for nbr in G[cur]:
            if nbr != pi:
                if nbr in path:
                    
                    circle = set()
                    in_circle = False
                    for e in path_list:
                        if e == nbr:
                            in_circle = True
                        if in_circle:
                            circle.add(e)
                    return circle

                path.add(nbr)
                path_list.append(nbr)
                circle = self.dfs(G, nbr, cur, path, path_list, visited)
                if circle:
                    return circle
                path.remove(nbr)
                path_list.pop()

        return None


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""R""e""d""u""n""d""a""n""t""C""o""n""n""e""c""t""i""o""n""(""[""[""1"",""2""]"","" ""[""1"",""3""]"","" ""[""2"",""3""]""]"")"" ""=""="" ""[""2"","" ""3""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""R""e""d""u""n""d""a""n""t""C""o""n""n""e""c""t""i""o""n""(""[""[""1"",""2""]"","" ""[""2"",""3""]"","" ""[""3"",""4""]"","" ""[""1"",""4""]"","" ""[""1"",""5""]""]"")"" ""=""="" ""[""1"","" ""4""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""R""e""d""u""n""d""a""n""t""C""o""n""n""e""c""t""i""o""n""(""[""[""3""0"",""4""4""]"",""[""3""4"",""4""7""]"",""[""2""2"",""3""2""]"",""[""3""5"",""4""4""]"",""[""2""6"",""3""6""]"",""[""2"",""1""5""]"",""[""3""8"",""4""1""]"",""[""2""8"",""3""5""]"",""[""2""4"",""3""7""]"",""[""1""4"",""4""9""]"",""[""4""4"",""4""5""]"",""[""1""1"",""5""0""]"",""[""2""0"",""3""9""]"",""[""7"",""3""9""]"",""[""1""9"",""2""2""]"",""[""3"",""1""7""]"",""[""1""5"",""2""5""]"",""[""1"",""3""9""]"",""[""2""6"",""4""0""]"",""[""5"",""1""4""]"",""[""6"",""2""3""]"",""[""5"",""6""]"",""[""3""1"",""4""8""]"",""[""1""3"",""2""2""]"",""[""4""1"",""4""4""]"",""[""1""0"",""1""9""]"",""[""1""2"",""4""1""]"",""[""1"",""1""2""]"",""[""3"",""1""4""]"",""[""4""0"",""5""0""]"",""[""1""9"",""3""7""]"",""[""1""6"",""2""6""]"",""[""7"",""2""5""]"",""[""2""2"",""3""3""]"",""[""2""1"",""2""7""]"",""[""9"",""5""0""]"",""[""2""4"",""4""2""]"",""[""4""3"",""4""6""]"",""[""2""1"",""4""7""]"",""[""2""9"",""4""0""]"",""[""3""1"",""3""4""]"",""[""9"",""3""1""]"",""[""1""4"",""3""1""]"",""[""5"",""4""8""]"",""[""3"",""1""8""]"",""[""4"",""1""9""]"",""[""8"",""1""7""]"",""[""3""8"",""4""6""]"",""[""3""5"",""3""7""]"",""[""1""7"",""4""3""]""]"")"" ""=""="" ""[""5"",""4""8""]""
