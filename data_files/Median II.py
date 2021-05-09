
__author__ = 'Danyang'
import heapq


class DualHeap(object):
    def __init__(self):
        
        self.min_h = []
        self.max_h = []

    def insert(self, num):
        if not self.min_h or num > self.min_h[0]:
            heapq.heappush(self.min_h, num)
        else:
            heapq.heappush(self.max_h, -num)
        self.balance()

    def balance(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        if l1-l2 > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            self.balance()
        elif l2-l1 > 1:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
            self.balance()
        return

    def get_median(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        m = (l1+l2-1)/2
        if m == l2-1:
            return -self.max_h[0]
        elif m == l2:
            return self.min_h[0]
        raise Exception("n"o"t" "b"a"l"a"n"c"e"d"")""
""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n"":""
"" "" "" "" ""d""e""f"" ""m""e""d""i""a""n""I""I""(""s""e""l""f"","" ""n""u""m""s"")"":""
"" "" "" "" "" "" "" "" 
        dh = DualHeap()
        ret = []
        for num in nums:
            dh.insert(num)
            ret.append(dh.get_median())
        return ret

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""e""d""i""a""n""I""I""(""[""4"","" ""5"","" ""1"","" ""3"","" ""2"","" ""6"","" ""0""]"")"" ""=""="" ""[""4"","" ""4"","" ""4"","" ""3"","" ""3"","" ""3"","" ""3""]""
""
""
