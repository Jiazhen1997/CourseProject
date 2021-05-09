

from typing import List
from collections import defaultdict
import heapq


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        counter = defaultdict(int)
        for e in nums:
            counter[e] += 1

        F = defaultdict(int)
        for e in nums:
            if counter[e] == 0:
                continue
            counter[e] -= 1

            if F[e - 1] > 0:
                F[e - 1] -= 1
                F[e] += 1
            elif counter[e + 1] > 0 and counter[e + 2] > 0:
                F[e + 2] += 1
                counter[e + 1] -= 1
                counter[e + 2] -= 1
            else:
                return False

        return True

            
class Interval:
    def __init__(self, end, length):
        self.end = end
        self.length = length

    def __lt__(self, other):
        if self.end == other.end:
            return self.length < other.length

        return self.end < other.end

    def __repr__(self):
        return repr((self.end, self.length))


class Solution2:
    def isPossible(self, nums: List[int]) -> bool:
        
        h = []
        for n in nums:
            while h and h[0].end + 1 < n:
                itvl = heapq.heappop(h)
                if itvl.length < 3:
                    return False

            if not h:
                heapq.heappush(h, Interval(n, 1))
            elif h[0].end + 1 == n:
                itvl = heapq.heappop(h)
                heapq.heappush(h, Interval(n, itvl.length + 1))
            else:  
                heapq.heappush(h, Interval(n, 1))


        for itvl in h:
            if itvl.length < 3:
                return False

        return True

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""P""o""s""s""i""b""l""e""(""[""1"",""2"",""3"",""3"",""4"",""5""]"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""P""o""s""s""i""b""l""e""(""[""1"",""2"",""3"",""3"",""4"",""4"",""5"",""5""]"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""P""o""s""s""i""b""l""e""(""[""1"",""2"",""3"",""4"",""4"",""5""]"")"" ""=""="" ""F""a""l""s""e""
