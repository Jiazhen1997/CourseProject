
__author__ = 'Danyang'


class Solution:
    def longestIncreasingSubsequence(self, nums):
        
        n = len(nums)
        if n == 0:
            return 0

        maxa = 1
        f = [1 for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(i):
                if nums[i] >= nums[j]:
                    f[i] = max(f[i], f[j]+1)

            maxa = max(maxa, f[i])

        return maxa  


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""I""n""c""r""e""a""s""i""n""g""S""u""b""s""e""q""u""e""n""c""e""(""
"" "" "" "" "" "" "" "" ""[""8""8"","" ""4"","" ""2""4"","" ""8""2"","" ""8""6"","" ""1"","" ""5""6"","" ""7""4"","" ""7""1"","" ""9"","" ""8"","" ""1""8"","" ""2""6"","" ""5""3"","" ""7""7"","" ""8""7"","" ""6""0"","" ""2""7"","" ""6""9"","" ""1""7"","" ""7""6"","" ""2""3"","" ""6""7"","" ""1""4"","" ""9""8"","" ""1""3"","" ""1""0"","" ""8""3"","" ""2""0"",""
"" "" "" "" "" "" "" "" "" ""4""3"","" ""3""9"","" ""2""9"","" ""9""2"","" ""3""1"","" ""0"","" ""3""0"","" ""9""0"","" ""7""0"","" ""3""7"","" ""5""9""]"")"" ""=""="" ""1""0