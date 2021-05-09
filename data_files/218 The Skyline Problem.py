

__author__ = 'Daniel'
from collections import defaultdict, namedtuple
import heapq


class Building(object):
    def __init__(self, h):
        self.h = h
        self.deleted = False  

    def __cmp__(self, other):
        
        assert isinstance(other, Building)
        return other.h - self.h



Event = namedtuple('Event', 'starts ends')


class Solution:
    def getSkyline(self, buildings):
        
        
        events = defaultdict(lambda: Event(starts=[], ends=[]))
        for left, right, height in buildings:
            building = Building(height)
            events[left].starts.append(building)  
            events[right].ends.append(building)

        heap_h = []  
        cur_h = 0  
        ret = []
        
        for x, event in sorted(events.items()):  
            for building in event.starts:
                heapq.heappush(heap_h, building)
            for building in event.ends:
                building.deleted = True

            
            
            while heap_h and heap_h[0].deleted:
                heapq.heappop(heap_h)

            
            
            new_h = heap_h[0].h if heap_h else 0

            if new_h != cur_h:
                cur_h = new_h
                ret.append([x, cur_h])

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""g""e""t""S""k""y""l""i""n""e""(""[""[""2"","" ""9"","" ""1""0""]"","" ""[""3"","" ""7"","" ""1""5""]"","" ""[""5"","" ""1""2"","" ""1""2""]"","" ""[""1""5"","" ""2""0"","" ""1""0""]"","" ""[""1""9"","" ""2""4"","" ""8""]""]"")"" ""=""="" ""\""
"" "" "" "" "" "" "" "" "" "" "" ""[""[""2"","" ""1""0""]"","" ""[""3"","" ""1""5""]"","" ""[""7"","" ""1""2""]"","" ""[""1""2"","" ""0""]"","" ""[""1""5"","" ""1""0""]"","" ""[""2""0"","" ""8""]"","" ""[""2""4"","" ""0""]""]