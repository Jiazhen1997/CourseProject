
__author__ = 'Daniel'



class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class SummaryRanges(object):
    def __init__(self):
        
        self.itvls = []

    def addNum(self, val):
        
        self.itvls.append(Interval(val, val))

    def getIntervals(self):
        
        self.itvls.sort(key=lambda x: x.start)

        ret = [self.itvls[0]]
        for itvl in self.itvls[1:]:
            pre = ret[-1]
            if itvl.start <= pre.end + 1:
                pre.end = max(itvl.end, pre.end)
            else:
                ret.append(itvl)

        self.itvls = ret
        return ret




