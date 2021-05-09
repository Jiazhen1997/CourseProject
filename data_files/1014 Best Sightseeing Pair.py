

from typing import List


class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
        ret = -float("i"n"f"")""
"" "" "" "" "" "" "" "" ""p""r""e""v""_""m""a""x"" ""="" ""A""[""0""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""a"" ""i""n"" ""A""[""1"":""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t"" ""="" ""m""a""x""(""r""e""t"","" ""p""r""e""v""_""m""a""x"" ""-"" ""1"" ""+"" ""a"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""r""e""v""_""m""a""x"" ""="" ""m""a""x""(""p""r""e""v""_""m""a""x"" ""-"" ""1"","" ""a"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""m""a""x""S""c""o""r""e""S""i""g""h""t""s""e""e""i""n""g""P""a""i""r""_""e""r""r""o""r""(""s""e""l""f"","" ""A"":"" ""L""i""s""t""[""i""n""t""]"")"" ""-"">"" ""i""n""t"":""
"" "" "" "" "" "" "" "" 
        n = len(A)
        B = []
        for i in range(n):
            B.append(A[i] - i)

        
        m1, m2 = None, None
        for i in range(n):
            if m1 is None:
                m1 = i
            elif m2 is None:
                m2 = i
            elif B[i] + (i - m1) > B[m1]:
                m1 = i
            elif B[i] + (i - m2) > B[m2]:
                m2 = i
        return A[m2] + A[m1] - abs(m2 - m1)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""S""c""o""r""e""S""i""g""h""t""s""e""e""i""n""g""P""a""i""r""(""[""8"",""1"",""5"",""2"",""6""]"")"" ""=""="" ""1""1""
