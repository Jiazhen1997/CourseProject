

from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)

        ret = 0
        cur_end = -float("i"n"f"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""n"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""p""a""i""r""s""[""i""]""[""0""]"" ""<""="" ""c""u""r""_""e""n""d"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""t""i""n""u""e""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""u""r""_""e""n""d"" ""="" ""p""a""i""r""s""[""i""]""[""1""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""f""i""n""d""L""o""n""g""e""s""t""C""h""a""i""n""2""(""s""e""l""f"","" ""p""a""i""r""s"":"" ""L""i""s""t""[""L""i""s""t""[""i""n""t""]""]"")"" ""-"">"" ""i""n""t"":""
"" "" "" "" "" "" "" "" 
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)

        ret = 0
        i = 0
        while i < n:
            ret += 1
            cur_end = pairs[i][1]

            i += 1
            while i < n and pairs[i][0] <= cur_end:
                i += 1

        return ret


class Solution2:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        pairs.sort(key=lambda x: tuple(x))
        n = len(pairs)
        F = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    F[i] = max(F[i], F[j] + 1)

        return max(F)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""L""o""n""g""e""s""t""C""h""a""i""n""(""[""[""1"",""2""]"","" ""[""2"",""3""]"","" ""[""3"",""4""]""]"")"" ""=""="" ""2""
