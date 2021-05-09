
__author__ = 'Daniel'


class Solution:
    def woodCut(self, L, k):
        
        if not L:
            return 0
        maxa = max(L)
        lo = 0
        hi = maxa+1
        while lo < hi:
            m = (lo+hi)/2
            if m == 0:
                return m
            cnt = 0
            for l in L:
                cnt += l/m
            if cnt >= k:
                lo = m+1
            else:
                hi = m

        return lo-1


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""w""o""o""d""C""u""t""(""[""2""1""4""7""4""8""3""6""4""4"","" ""2""1""4""7""4""8""3""6""4""5"","" ""2""1""4""7""4""8""3""6""4""6"","" ""2""1""4""7""4""8""3""6""4""7""]"","" ""4"")"" ""=""="" ""2""1""4""7""4""8""3""6""4""4