
__author__ = 'Danyang'


class QueueNode(object):
    def __init__(self, val):
        self.val = val
        self.q = [val]  

    def __cmp__(self, other):
        return self.val-other.val

    def __repr__(self):
        return repr(self.val)

    def next(self):
        self.q.pop(0)
        self.val = self.q[0]


class Solution:
    def kthPrimeNumber(self, k):
        
        import heapq

        h1 = QueueNode(3)
        h2 = QueueNode(5)
        h3 = QueueNode(7)

        heap = [h1, h2, h3]
        heapq.heapify(heap)

        for cnt in xrange(k-1):
            h = heapq.heappop(heap)
            if h == h1:
                h1.q.append(h1.val*3)
                h2.q.append(h1.val*5)
                h3.q.append(h1.val*7)
            elif h == h2:
                h2.q.append(h2.val*5)
                h3.q.append(h2.val*7)
            else:
                h3.q.append(h3.val*7)

            h.next()
            heapq.heappush(heap, h)

        return heapq.heappop(heap).val

    def kthPrimeNumber_error(self, k):
        
        import heapq

        h1 = QueueNode(3)
        h2 = QueueNode(5)
        h3 = QueueNode(7)

        heap = [h1, h2, h3]
        heapq.heapify(heap)

        for cnt in xrange(k-1):
            h = heapq.heappop(heap)
            if h == h1:
                for i in [3, 5, 7]:
                    h1.q.append(i*h1.val)

                h1.next()
                heapq.heappush(heap, h1)
            elif h == h2:
                for i in [5, 7]:
                    h2.q.append(i*h2.val)

                h2.next()
                heapq.heappush(heap, h2)
            else:
                for i in [7]:
                    h3.q.append(i*h3.val)

                h3.next()
                heapq.heappush(heap, h3)

        return heapq.heappop(heap).val


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""t""h""P""r""i""m""e""N""u""m""b""e""r""(""3""2""1"")"" ""=""="" ""1""4""5""8""6""0""7""5