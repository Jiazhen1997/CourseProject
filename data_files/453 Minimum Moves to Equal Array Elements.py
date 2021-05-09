



class Solution:
    def minMoves(self, nums):
        
        mini = min(nums)
        return sum(map(lambda e: e - mini, nums))


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""M""o""v""e""s""(""[""1"","" ""2"","" ""3""]"")"" ""=""="" ""3""
