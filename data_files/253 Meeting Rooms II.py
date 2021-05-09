
import heapq
import operator


__author__ = 'Daniel'


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def minMeetingRooms(self, intervals):
        
        maxa = 0

        intervals.sort(key=operator.attrgetter("s"t"a"r"t"")"")""
"" "" "" "" "" "" "" "" ""h""_""e""n""d"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i""t""v""l"" ""i""n"" ""i""n""t""e""r""v""a""l""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""h""e""a""p""q"".""h""e""a""p""p""u""s""h""(""h""_""e""n""d"","" ""i""t""v""l"".""e""n""d"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""h""_""e""n""d"" ""a""n""d"" ""h""_""e""n""d""[""0""]"" ""<""="" ""i""t""v""l"".""s""t""a""r""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""h""e""a""p""q"".""h""e""a""p""p""o""p""(""h""_""e""n""d"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""a""x""a"" ""="" ""m""a""x""(""m""a""x""a"","" ""l""e""n""(""h""_""e""n""d"")"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""m""a""x""a