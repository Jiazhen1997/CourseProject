
__author__ = 'Daniel'


class Solution(object):
    def findDuplicate(self, nums):
        
        f, s = 0, 0
        while True:
            f = nums[nums[f]]
            s = nums[s]
            if f == s:
                break

        t = 0
        while t != s:
            t = nums[t]
            s = nums[s]

        return t


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""D""u""p""l""i""c""a""t""e""(""[""1"","" ""2"","" ""3"" "",""4"","" ""5"","" ""5""]"")"" ""=""="" ""5""
""
