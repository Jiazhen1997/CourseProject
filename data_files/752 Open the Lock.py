

from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        destination = tuple(int(c) for c in target)
        deadends_set = set(
            tuple(int(c) for c in s)
            for s in deadends
        )
        q = [(0, 0, 0, 0)]
        if q[0] in deadends_set:
            return -1

        step = 0
        visited = set(q)
        while q:
            cur_q = []
            for e in q:
                if e == destination:
                    return step
                for i in range(4):
                    for delta in (-1, 1):
                        nxt_lst = list(e)  
                        nxt_lst[i] = (nxt_lst[i] + delta) % 10  
                        nxt = tuple(nxt_lst)
                        if nxt not in visited and nxt not in deadends_set:
                            visited.add(nxt)
                            cur_q.append(nxt)

            step += 1
            q = cur_q

        return -1


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""o""p""e""n""L""o""c""k""(""[