
__author__ = 'Daniel'

import bisect


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        
        if a == 0:
            ret = map(lambda x: self.f(x, a, b, c), nums)
            return ret if b > 0 else ret[::-1]

        mid = - float(b) / (2*a)
        ri = bisect.bisect_left(nums, mid)
        le = ri - 1
        ret = []
        while le >= 0 and ri < len(nums) and le < ri:
            f_le = self.f(nums[le], a, b, c)
            f_ri = self.f(nums[ri], a, b, c)
            if a > 0 and f_le < f_ri or a < 0 and f_le > f_ri:
                ret.append(f_le)
                le -= 1
            else:
                ret.append(f_ri)
                ri += 1

        while le >= 0:
            ret.append(self.f(nums[le], a, b, c))
            le -= 1
        while ri < len(nums):
            ret.append(self.f(nums[ri], a, b, c))
            ri += 1

        return ret if a > 0 else ret[::-1]

    def f(self, x, a, b, c):
        return a * (x ** 2) + b * x + c


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""o""r""t""T""r""a""n""s""f""o""r""m""e""d""A""r""r""a""y""(""[""-""4"","" ""-""2"","" ""2"","" ""4""]"","" ""-""1"","" ""3"","" ""5"")"" ""=""="" ""[""-""2""3"","" ""-""5"","" ""1"","" ""7""]