
__author__ = 'Danyang'



class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, itvls):
        
        if not itvls:
            return []

        itvls.sort(key=lambda x: x.start)  
        ret = [itvls[0]]
        for cur in itvls[1:]:
            pre = ret[-1]
            if cur.start <= pre.end:  
                pre.end = max(pre.end, cur.end)
            else:
                ret.append(cur)

        return ret

    def merge_error(self, itvls):
        
        if not itvls:
            return []

        ret = [itvls[0]]
        for interval in itvls[1:]:
            if ret[-1].end < interval.start:
                ret.append(interval)
                continue
            if ret[-1].start <= interval.start <= ret[-1].end <= interval.end:
                ret[-1].end = interval.end
                continue
            if interval.start <= ret[-1].start and ret[-1].end <= interval.end:
                ret[-1] = interval
                continue
            if ret[-1].start <= interval.start < ret[-1].end and ret[-1].start <= interval.end < ret[-1].end:
                ret.append(interval)
                continue
            if interval.start < ret[-1].start <= interval.end < ret[-1].end:
                ret[-1].start = interval.start
                continue
            if interval.end < ret[-1].start:
                ret.append(ret)
                continue

        return ret
