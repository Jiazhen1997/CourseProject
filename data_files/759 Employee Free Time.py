

from typing import List
import heapq


S = 0
E = 1


class Solution:
    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        
        cur_max_end = min(
            itv[E]
            for itvs in schedule
            for itv in itvs
        )
        q = []
        for i, itvs in enumerate(schedule):
            
            j = 0
            itv = itvs[j]
            heapq.heappush(q, (itv[S], i, j))

        ret = []
        while q:
            _, i, j = heapq.heappop(q)
            itv = schedule[i][j]
            if cur_max_end < itv[S]:
                ret.append([cur_max_end, itv[S]])

            cur_max_end = max(cur_max_end, itv[E])

            
            j += 1
            if j < len(schedule[i]):
                itv = schedule[i][j]
                heapq.heappush(q, (itv[S], i, j))

        return ret

    def employeeFreeTime(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        
        
        lst = []
        for itvs in schedule:
            for itv in itvs:
                lst.append([itv[S], S])
                lst.append([itv[E], E])

        lst.sort()
        count = 0
        prev = None
        ret = []
        for t, flag in lst:
            if count == 0 and prev:
                ret.append([prev, t])

            if flag == S:
                count += 1
            else:
                prev = t
                count -= 1

        return ret

    def employeeFreeTime_error(self, schedule: List[List[List[int]]]) -> List[List[int]]:
        
        schedules = list(map(iter, schedule))
        cur_max_end = min(
            itv[E]
            for emp in schedule
            for itv in emp
        )
        q = []
        for emp_iter in schedules:
            itv = next(emp_iter, None)
            if itv:
                heapq.heappush(q, (itv[S], itv, emp_iter))

        ret = []
        while q:
            _, itv, emp_iter = heapq.heappop(q)
            if cur_max_end < itv[S]:
                ret.append([cur_max_end, itv[S]])
            cur_max_end = max(cur_max_end, itv[E])
            itv = next(emp_iter, None)
            if itv:
                heapq.heappush(q, (itv[S], itv, emp_iter))

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""e""m""p""l""o""y""e""e""F""r""e""e""T""i""m""e""(""[""[""[""1"",""2""]"",""[""5"",""6""]""]"",""[""[""1"",""3""]""]"",""[""[""4"",""1""0""]""]""]"")"" ""=""="" ""[""[""3"",""4""]""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""e""m""p""l""o""y""e""e""F""r""e""e""T""i""m""e""(""[""[""[""4"",""1""6""]"",""[""3""1"",""3""6""]"",""[""4""2"",""5""0""]"",""[""8""0"",""8""3""]"",""[""9""5"",""9""6""]""]"",""[""[""4"",""1""3""]"",""[""1""4"",""1""9""]"",""[""3""7"",""5""3""]"",""[""6""4"",""6""6""]"",""[""8""5"",""8""9""]""]"",""[""[""1""7"",""2""4""]"",""[""3""8"",""3""9""]"",""[""4""9"",""5""1""]"",""[""6""2"",""6""7""]"",""[""7""9"",""8""1""]""]"",""[""[""9"",""1""5""]"",""[""1""7"",""2""4""]"",""[""4""5"",""6""3""]"",""[""6""5"",""6""8""]"",""[""8""7"",""8""8""]""]"",""[""[""1""7"",""3""3""]"",""[""3""9"",""4""1""]"",""[""4""3"",""5""7""]"",""[""5""8"",""6""3""]"",""[""7""0"",""8""4""]""]""]"")"" ""=""="" ""[""[""3""6"","" ""3""7""]"","" ""[""6""8"","" ""7""0""]"","" ""[""8""4"","" ""8""5""]"","" ""[""8""9"","" ""9""5""]""]""
