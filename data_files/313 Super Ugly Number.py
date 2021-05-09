

import heapq
from collections import deque
import sys

__author__ = 'Daniel'


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        
        k = len(primes)
        ret = [sys.maxint for _ in xrange(n)]
        ret[0] = 1
        
        idxes = [0 for _ in xrange(k)]
        for i in xrange(1, n):
            for j in xrange(k):
                ret[i] = min(ret[i], primes[j]*ret[idxes[j]])

            for j in xrange(k):
                if ret[i] == primes[j]*ret[idxes[j]]:
                    idxes[j] += 1

        return ret[n-1]


class QueueWrapper(object):
    def __init__(self, idx, q):
        self.idx = idx
        self.q = q

    def __cmp__(self, other):
        return self.q[0] - other.q[0]


class SolutionHeap(object):
    def nthSuperUglyNumber(self, n, primes):
        
        ret = 1
        h = [QueueWrapper(i, deque([v])) for i, v in enumerate(primes)]
        dic = {e.idx: e for e in h}

        heapq.heapify(h)
        for _ in xrange(n-1):
            mini = heapq.heappop(h)
            ret = mini.q.popleft()
            for i in xrange(mini.idx, len(primes)):
                dic[i].q.append(ret*primes[i])
            heapq.heappush(h, mini)

        return ret

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""t""h""S""u""p""e""r""U""g""l""y""N""u""m""b""e""r""(""1""2"","" ""[""2"","" ""7"","" ""1""3"","" ""1""9""]"")"" ""=""="" ""3""2