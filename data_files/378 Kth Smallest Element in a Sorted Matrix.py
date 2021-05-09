
import heapq


__author__ = 'Daniel'


class Solution(object):
    def kthSmallest(self, matrix, k):
        
        m, n = len(matrix), len(matrix[0])

        class Node(object):
            def __init__(self, i, j):
                self.i = i
                self.j = j

            def __cmp__(self, other):
                return matrix[self.i][self.j] - matrix[other.i][other.j]

            def hasnext(self):
                return self.j+1 < n

            def next(self):
                if self.hasnext():
                    return Node(self.i, self.j + 1)

                raise StopIteration

        h = []
        for i in xrange(m):
            heapq.heappush(h, Node(i, 0))

        ret = None
        for _ in xrange(k):
            ret = heapq.heappop(h)
            if ret.hasnext():
                heapq.heappush(h, ret.next())

        return matrix[ret.i][ret.j]

    def kthSmallestError(self, matrix, k):
        
        m, n = len(matrix), len(matrix[0])
        i = k % n
        j = k - (i * m)
        return matrix[i][j]

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""m""a""t""r""i""x"" ""="" ""[""
"" "" "" "" "" "" "" "" ""[""1"","" ""5"","" ""9""]"",""
"" "" "" "" "" "" "" "" ""[""1""0"","" ""1""1"","" ""1""3""]"",""
"" "" "" "" "" "" "" "" ""[""1""2"","" ""1""3"","" ""1""5""]""
"" "" "" "" ""]""
"" "" "" "" ""k"" ""="" ""8""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""k""t""h""S""m""a""l""l""e""s""t""(""m""a""t""r""i""x"","" ""k"")""
