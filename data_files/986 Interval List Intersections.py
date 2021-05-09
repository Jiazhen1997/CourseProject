

from typing import List



class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        
        i, j = 0, 0
        m, n = len(A), len(B)
        ret = []
        while i < m and j < n:
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if lo <= hi:
                ret.append(Interval(lo, hi))
            if A[i].end > B[j].end:
                j += 1
            else:
                i += 1

        return ret

    def intervalIntersection_complex(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        
        ret = []
        i = 0
        j = 0
        m, n = len(A), len(B)
        while i < m and j < n:
            a = A[i]
            b = B[j]
            if b.start <= a.end <= b.end:
                ret.append(Interval(max(a.start, b.start), a.end))
                i += 1
            elif a.start <= b.end <= a.end:
                ret.append(Interval(max(a.start, b.start), b.end))
                j += 1
            else:
                if a.end < b.start:
                    i += 1
                else:
                    j += 1
        return ret
