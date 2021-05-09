
import operator

__author__ = 'Daniel'


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def canAttendMeetings(self, intervals):
        
        intervals.sort(key=operator.attrgetter("s"t"a"r"t"")"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""(""i""n""t""e""r""v""a""l""s"")""-""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""i""n""t""e""r""v""a""l""s""[""i""]"".""e""n""d"" "">"" ""i""n""t""e""r""v""a""l""s""[""i""+""1""]"".""s""t""a""r""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""F""a""l""s""e""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""T""r""u""e""
""
