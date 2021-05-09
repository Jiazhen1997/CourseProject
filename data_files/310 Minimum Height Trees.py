
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def findMinHeightTrees(self, n, edges):
        
        if not edges:
            return [0]

        V = {i: [] for i in xrange(n)}
        for a, b in edges:
            V[a].append(b)
            V[b].append(a)

        
        _, _, last = self.bfs(0, V)
        level, pi, last = self.bfs(last, V)

        ret = []
        cur = last
        for _ in xrange((level-1)/2):
            cur = pi[cur]
        ret.append(cur)

        if level%2 == 0:
            ret.append(pi[cur])

        return ret

    def bfs(self, s, V):
        
        visited = [False for _ in xrange(len(V))]
        pi = [-1 for _ in xrange(len(V))]
        last = s
        level = 0
        q = []
        q.append(s)
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                last = cur
                visited[cur] = True
                for nbr in V[cur]:
                    if not visited[nbr]:
                        pi[nbr] = cur
                        q.append(nbr)

            q = q[l:]
            level += 1

        return level, pi, last


class Solution_TLE(object):
    def findMinHeightTrees_TLE(self, n, edges):
        
        if not edges:
            return 0

        V = {i: [] for i in xrange(n)}
        for a, b in edges:
            V[a].append(b)
            V[b].append(a)

        ret = []
        mini = n
        for k in V.keys():
            l = self.bfs(k, V)
            if l < mini:
                ret = [k]
                mini = l
            elif l == mini:
                ret.append(k)

        return ret

    def bfs(self, s, V):
        
        visisted = [False for _ in xrange(len(V))]
        q = []
        level = 0
        q.append(s)
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                visisted[cur] = True
                for nbr in V[cur]:
                    if not visisted[nbr]:
                        q.append(nbr)

            q = q[l:]
            level += 1

        return level


class SolutionError(object):
    def findMinHeightTrees(self, n, edges):
        
        if not edges:
            return 0

        V = {i: [] for i in xrange(n)}
        for a, b in edges:
            V[a].append(b)
            V[b].append(a)

        leaf = None
        for k, v in V.items():
            if len(v) == 1:
                leaf = k
                break

        
        visisted = [False for _ in xrange(n)]
        h2v = defaultdict(list)
        q = []
        level = 0
        q.append(leaf)
        while q:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                h2v[level].append(cur)
                visisted[cur] = True
                for nbr in V[cur]:
                    if not visisted[nbr]:
                        q.append(nbr)

            q = q[l:]
            level += 1

        if level%2 == 0:
            return h2v[level/2-1]+h2v[level/2]
        else:
            return h2v[level/2]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""#"" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""i""n""H""e""i""g""h""t""T""r""e""e""s""(""6"","" ""[""[""3"",""0""]"",""[""3"",""1""]"",""[""3"",""2""]"",""[""3"",""4""]"",""[""5"",""4""]""]"")""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""i""n""H""e""i""g""h""t""T""r""e""e""s""(""7"","" ""[""[""0"","" ""1""]"","" ""[""1"","" ""2""]"","" ""[""1"","" ""3""]"","" ""[""2"","" ""4""]"","" ""[""3"","" ""5""]"","" ""[""4"","" ""6""]""]"")"" ""=""="" ""[""1"","" ""2""]