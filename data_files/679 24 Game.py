

from typing import List


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.dfs(nums, {})

    def dfs(self, A, cache):
        if tuple(A) not in cache:
            n = len(A)
            if n == 1:
                return abs(A[0] - 24) < 0.001

            for i in range(n):
                for j in range(i):
                    a = A[i]
                    b = A[j]
                    for c in (a+b, a-b, b-a, a*b, b and a/b, a and b/a):
                        
                        A_new = A[:j] + A[j+1:i] + A[i+1:] + [c]
                        A_new.sort()
                        if self.dfs(A_new, cache):
                            cache[tuple(A)] = True
                            return cache[tuple(A)]

            cache[tuple(A)] = False

        return cache[tuple(A)]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""j""u""d""g""e""P""o""i""n""t""2""4""(""[""4"","" ""1"","" ""8"","" ""7""]"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""j""u""d""g""e""P""o""i""n""t""2""4""(""[""1"","" ""2"","" ""1"","" ""2""]"")"" ""=""="" ""F""a""l""s""e""
