

import heapq


class Balloon:
    def __init__(self, s, e):
        self.s = s
        self.e = e

    def __lt__(self, other):
        
        return self.e < other.e


class Solution:
    def findMinArrowShots(self, points):
        
        ret = 0
        points.sort(key=lambda x: x[0])
        heap = []
        for point in points:
            s, e = point
            if heap and heap[0].e < s:
                ret += 1
                heap = []

            heapq.heappush(heap, Balloon(s, e))

        if heap:
            ret += 1

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""i""n""A""r""r""o""w""S""h""o""t""s""(""[""[""1""0"",""1""6""]"","" ""[""2"",""8""]"","" ""[""1"",""6""]"","" ""[""7"",""1""2""]""]"")"" ""=""="" ""2""
