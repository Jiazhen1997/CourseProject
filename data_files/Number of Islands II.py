
import random

__author__ = 'Daniel'


class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __repr__(self):
        return "["%"d"," "%"d"]"" ""%"" ""(""s""e""l""f"".""x"","" ""s""e""l""f"".""y"")""
""
""
""c""l""a""s""s"" ""U""n""i""o""n""F""i""n""d""(""o""b""j""e""c""t"")"":""
"" "" "" "" 

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


class Solution:
    def __init__(self):
        self.dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

    def numIslands2(self, n, m, operators):
        
        rows = n
        cols = m
        unroll = lambda x, y: x*cols+y  
        mat = [[0 for _ in xrange(cols)] for _ in xrange(rows)]
        uf = UnionFind(rows, cols)
        ret = []
        for op in operators:
            uf.add(unroll(op.x, op.y))
            mat[op.x][op.y] = 1
            for dir in self.dirs:
                x1 = op.x+dir[0]
                y1 = op.y+dir[1]
                if 0 <= x1 < rows and 0 <= y1 < cols and mat[x1][y1] == 1:
                    uf.union(unroll(op.x, op.y), unroll(x1, y1))

            ret.append(uf.count)

        return ret


class TestCaseGenerator(object):
    def _generate(self):
        dim = 10
        m = random.randrange(1, dim)
        n = random.randrange(1, dim)
        k = random.randrange(1, max(2, m*n/3))
        operators = []
        visited = set()
        while len(operators) < k:
            p = random.randrange(m*n)
            if p not in visited:
                x = p/n
                y = p%n
                operators.append(Point(x, y))
                visited.add(p)

        print(m)
        print(n)
        print(operators)

    def generate(self, T=50):
        for _ in xrange(T):
            self._generate()


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""I""s""l""a""n""d""s""2""(""3"","" ""3"","" ""m""a""p""(""l""a""m""b""d""a"" ""x"":"" ""P""o""i""n""t""(""x""[""0""]"","" ""x""[""1""]"")"","" ""[""(""0"","" ""0"")"","" ""(""0"","" ""1"")"","" ""(""2"","" ""2"")"","" ""(""2"","" ""1"")""]"")"")"" ""=""="" ""[""1"","" ""1"","" ""2"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""2""]""
"" "" "" "" ""t""e""s""t""c""a""s""e"" ""="" ""T""e""s""t""C""a""s""e""G""e""n""e""r""a""t""o""r""("")""
"" "" "" "" ""t""e""s""t""c""a""s""e"".""g""e""n""e""r""a""t""e""("")""
