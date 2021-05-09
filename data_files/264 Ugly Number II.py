
import heapq


__author__ = 'Daniel'


class Node(object):
    
    def __init__(self, origin, q):
        self.origin = origin
        self.q = q

    def __cmp__(self, other):
        return self.q[0] - other.q[0]


class Solution(object):
    def nthUglyNumber(self, n):
        
        if n == 1:
            return 1

        n -= 1  

        ugly = [2, 3, 5]
        qs = [Node(i, [i]) for i in ugly]
        h = list(qs)  

        heapq.heapify(h)

        cnt = 0
        ret = 2
        while cnt < n:
            cnt += 1
            popped = heapq.heappop(h)
            ret = popped.q.pop(0)
            for i in xrange(ugly.index(popped.origin), 3):
                qs[i].q.append(ret*ugly[i])

            heapq.heappush(h, popped)

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""t""h""U""g""l""y""N""u""m""b""e""r""(""1""0"")"" ""=""="" ""1""2""
