
__author__ = 'Daniel'
from collections import defaultdict


class Heap(object):
    def __init__(self, A):
        
        self._A = A  
        self._h = []  
        self._pos = defaultdict(set)  

    def _pos2pos_set(self, ind):
        return self._pos[self._A[self._h[ind]]]

    def _swap_heap_node(self, i, j):
        if self._cmp_by_pos(i, j) == 0:
            return

        self._pos2pos_set(i).remove(i)
        self._pos2pos_set(j).remove(j)
        self._pos2pos_set(i).add(j)
        self._pos2pos_set(j).add(i)
        self._h[i], self._h[j] = self._h[j], self._h[i]

    def _pi(self, pos):
        
        if pos%2 == 0:
            return max(0, pos/2-1)
        else:
            return pos/2

    def push(self, i):
        pos = len(self._h)
        self._h.append(i)
        self._pos[self._A[i]].add(pos)

        pi = self._pi(pos)
        while pi != pos and self._cmp_by_pos(pos, pi) < 0:
            self._swap_heap_node(pi, pos)

            pos = pi
            pi = self._pi(pos)

    def _val2pos(self, val):
        return next(iter(self._pos[val]))

    def _pos2val(self, pos):
        return self._A[self._h[pos]]

    def _cmp_by_pos(self, i, j):
        return self._pos2val(i) - self._pos2val(j)

    def remove(self, i):
        try:
            pos = self._val2pos(self._A[i])
            self.pop(pos)
        except StopIteration:
            
            pass

    def _heappush(self, pos):
        
        n = len(self._h)
        if pos >= n:
            return

        l = 2*pos+1
        r = 2*pos+2
        mini = pos
        if l < n and self._cmp_by_pos(l, mini) < 0:
            mini = l
        if r < n and self._cmp_by_pos(r, mini) < 0:
            mini = r
        if pos != mini:
            self._swap_heap_node(pos, mini)
            self._heappush(mini)

    def peek(self):
        return self._h[0]

    def pop(self, pos=0):
        
        last_pos = len(self._h)-1
        self._swap_heap_node(pos, last_pos)

        
        self._pos2pos_set(last_pos).remove(last_pos)
        head = self._h.pop()

        
        self._heappush(pos)
        return head

    def __len__(self):
        return len(self._h)

    def __repr__(self):
        return repr(map(lambda x: self._A[x], self._h))


class DualHeap(object):
    def __init__(self, A):
        self._A = A
        self.min_h = Heap(A)  
        self.max_h = Heap(map(lambda x: -x, A))  

    def _rebalance(self):
        r = len(self.min_h)
        l = len(self.max_h)
        if abs(l-r) <= 1:
            return

        if r > l:
            self.max_h.push(self.min_h.pop())
        else:
            self.min_h.push(self.max_h.pop())

        self._rebalance()

    def add(self, i):
        if len(self.min_h) > 0 and self._A[i] > self._A[self.min_h.peek()]:
            self.min_h.push(i)
        else:
            self.max_h.push(i)

        self._rebalance()

    def remove(self, i):
        if len(self.min_h) > 0 and self._A[i] >= self._A[self.min_h.peek()]:
            self.min_h.remove(i)
        else:
            self.max_h.remove(i)

        self._rebalance()

    def median(self):
        r = len(self.min_h)
        l = len(self.max_h)
        if r > l:
            return self._A[self.min_h.peek()]
        else:
            return self._A[self.max_h.peek()]

    def __repr__(self):
        return repr(self.max_h)+repr(self.min_h)


class Solution:
    def medianSlidingWindow(self, nums, k):
        
        if len(nums) < 1:
            return []

        ret = []
        dh = DualHeap(nums)
        for i in xrange(k):
            dh.add(i)
        ret.append(dh.median())

        for i in xrange(k, len(nums)):
            dh.remove(i-k)
            dh.add(i)
            ret.append(dh.median())

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""S""l""i""d""i""n""g""W""i""n""d""o""w""(""[""1"","" ""1"","" ""1"","" ""1""]"","" ""3"")"" ""=""="" ""[""1"","" ""1""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""S""l""i""d""i""n""g""W""i""n""d""o""w""(""[""1"","" ""2"","" ""7"","" ""8"","" ""5""]"","" ""3"")"" ""=""="" ""[""2"","" ""7"","" ""7""]