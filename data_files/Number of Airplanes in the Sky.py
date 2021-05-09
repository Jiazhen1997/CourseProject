
__author__ = 'Daniel'


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    @staticmethod
    def cmp(a, b):
        
        if a.start != b.start:
            return a.start-b.start
        else:
            return a.end-b.end

    def countOfAirplanes(self, airplanes):
        
        return self.count_heap(airplanes)

    def count_heap(self, intervals):
        
        import heapq

        intervals.sort(cmp=Solution.cmp)
        heap = []
        cnt = 0
        for intv in intervals:
            
            heapq.heappush(heap, intv.end)
            
            while heap[0] <= intv.start:
                heapq.heappop(heap)

            cnt = max(cnt, len(heap))

        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""u""n""t""O""f""A""i""r""p""l""a""n""e""s""(""[""I""n""t""e""r""v""a""l""(""i""[""0""]"","" ""i""[""1""]"")"" ""f""o""r"" ""i"" ""i""n"" ""[""[""1"","" ""1""0""]"","" ""[""2"","" ""3""]"","" ""[""5"","" ""8""]"","" ""[""4"","" ""7""]""]""]"")"" ""=""="" ""3