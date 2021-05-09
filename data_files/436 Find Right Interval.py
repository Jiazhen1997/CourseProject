

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def new(cls, lst):
        return [
            cls(s, e)
            for s, e in lst
        ]

from bisect import bisect_left


class Solution:
    def findRightInterval(self, intervals):
        
        indexes = {
            itv.start: idx
            for idx, itv in enumerate(intervals)
        }
        starts = list(sorted(indexes.keys()))
        ret = []
        for itv in intervals:
            idx = bisect_left(starts, itv.end)
            if idx >= len(starts):
                ret.append(-1)
            else:
                ret.append(
                    indexes[starts[idx]]
                )

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""R""i""g""h""t""I""n""t""e""r""v""a""l""(""I""n""t""e""r""v""a""l"".""n""e""w""(""["" ""[""3"",""4""]"","" ""[""2"",""3""]"","" ""[""1"",""2""]"" ""]"")"")"" ""=""="" ""[""-""1"","" ""0"","" ""1""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""R""i""g""h""t""I""n""t""e""r""v""a""l""(""I""n""t""e""r""v""a""l"".""n""e""w""(""["" ""[""1"",""2""]"" ""]"")"")"" ""=""="" ""[""-""1""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""R""i""g""h""t""I""n""t""e""r""v""a""l""(""I""n""t""e""r""v""a""l"".""n""e""w""(""["" ""[""1"",""4""]"","" ""[""2"",""3""]"","" ""[""3"",""4""]"" ""]"")"")"" ""=""="" ""[""-""1"","" ""2"","" ""-""1""]""
