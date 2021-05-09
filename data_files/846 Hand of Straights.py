

from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def isNStraightHand(self, A: List[int], W: int) -> bool:
        
        q = deque()
        counter = Counter(A)
        prev = 0
        prev_cnt = 0
        for k in sorted(counter):  
            if prev_cnt > counter[k] or prev_cnt > 0 and k > prev + 1:
                return False
                
            q.append(counter[k] - prev_cnt)
            prev, prev_cnt = k, counter[k]
            if len(q) == W:
                c = q.popleft()
                prev_cnt -= c

        return prev_cnt == 0

    def isNStraightHand_heap(self, A: List[int], W: int) -> bool:
        
        A.sort()
        if len(A) % W != 0:
            return False
        if W == 1:
            return True


        h = []  
        for a in A:
            if not h:
                h = [(a, [a])]
                continue

            if a == h[0][1][-1]:
                heapq.heappush(h, (a, [a]))
            elif a == h[0][1][-1] + 1:
                _, lst = heapq.heappop(h)
                lst.append(a)
                if len(lst) < W:
                    heapq.heappush(h, (a, lst))
            else:
                return False

        if h:
            return False

        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""N""S""t""r""a""i""g""h""t""H""a""n""d""(""[""1"",""2"",""3"",""6"",""2"",""3"",""4"",""7"",""8""]"","" ""3"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""i""s""N""S""t""r""a""i""g""h""t""H""a""n""d""(""[""1"",""1"",""2"",""2"",""3"",""3""]"","" ""3"")"" ""=""="" ""T""r""u""e""
