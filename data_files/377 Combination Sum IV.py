
__author__ = 'Daniel'


class Solution(object):
    def combinationSum4(self, nums, target):
        
        F = [0 for _ in xrange(target + 1)]
        nums = filter(lambda x: x <= target, nums)
        for k in nums:
            F[k] = 1

        for i in xrange(target + 1):
            for k in nums:
                if i - k >= 0:
                    F[i] += F[i-k]

        return F[target]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""m""b""i""n""a""t""i""o""n""S""u""m""4""(""[""1"","" ""2"","" ""3""]"","" ""4"")"" ""=""="" ""7""
