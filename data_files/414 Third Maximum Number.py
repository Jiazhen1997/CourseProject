

__author__ = 'Danyang'
import heapq


class Solution:
    def thirdMax(self, nums):
        
        if not nums:
            return None

        h = []
        for e in set(nums):
            if len(h) < 3:
                heapq.heappush(h, e)
            elif len(h) == 3 and e > h[0]:
                heapq.heappushpop(h, e)

        assert len(h) <= 3
        if len(h) == 3:
            ret = min(h)
        else:
            ret = max(h)
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""t""h""i""r""d""M""a""x""(""[""1"","" ""2"","" ""3"","" ""4""]"")"" ""=""="" ""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""t""h""i""r""d""M""a""x""(""[""4"","" ""3"","" ""2"","" ""1""]"")"" ""=""="" ""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""t""h""i""r""d""M""a""x""(""[""2"","" ""2"","" ""3"","" ""1""]"")"" ""=""="" ""1""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""t""h""i""r""d""M""a""x""(""[""4"","" ""3""]"")"" ""=""="" ""4""
