
__author__ = 'Daniel'
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
        if l1 - l2 > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            self.balance()
        elif l2 - l1 > 1:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
            self.balance()
        return

    def get_median(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        m = (l1 + l2 - 1) / 2
        if (l1 + l2) % 2 == 1:
            if m == l2 - 1:
                return -self.max_h[0]
            elif m == l2:
                return self.min_h[0]
            raise Exception("n"o"t" "b"a"l"a"n"c"e"d"")""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""(""-""s""e""l""f"".""m""a""x""_""h""[""0""]"" ""+"" ""s""e""l""f"".""m""i""n""_""h""[""0""]"")"" ""/"" ""2"".""0""
""
""
""c""l""a""s""s"" ""S""o""l""u""t""i""o""n"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""d""h"" ""="" ""D""u""a""l""H""e""a""p""("")""
""
"" "" "" "" ""d""e""f"" ""s""o""l""v""e""(""s""e""l""f"","" ""c""i""p""h""e""r"")"":""
"" "" "" "" "" "" "" "" 
        self.dh.insert(cipher)
        return self.dh.get_median()


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(