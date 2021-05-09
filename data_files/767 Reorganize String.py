

from collections import defaultdict


class Solution:
    def reorganizeString(self, S: str) -> str:
        
        counter = defaultdict(int)
        for c in S:
            counter[c] += 1

        lst = [
            (-n, n, c)
            for c, n in counter.items()
        ]
        lst.sort()
        piles = []
        _, n, c = lst[0]
        for i in range(n):
            piles.append([c])

        cnt = 0
        for _, n, c in lst[1:]:
            for _ in range(n):
                piles[cnt].append(c)
                cnt = (cnt + 1) % len(piles)

        if len(piles) > 1 and len(piles[-2]) == 1:
            return ""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 