

from bisect import bisect


class Solution:
    def nextGreaterElements(self, nums):
        
        
        stk = []
        for n in nums[::-1]:
            while stk and stk[-1] <= n:
                stk.pop()
            stk.append(n)

        ret = []
        for n in nums[::-1]:
            while stk and stk[-1] <= n:
                stk.pop()
            ret.append(stk[-1] if stk else -1)
            stk.append(n)

        return ret[::-1]

    def nextGreaterElements_error(self, nums):
        
        A = nums + nums
        print(A)
        ret = []
        for e in nums:
            t = bisect(A, e)
            if t == len(A):
                ret.append(-1)
            else:
                ret.append(A[t])

        print(ret)
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""e""x""t""G""r""e""a""t""e""r""E""l""e""m""e""n""t""s""(""[""1"",""2"",""1""]"")"" ""=""="" ""[""2"","" ""-""1"","" ""2""]""
