

from typing import List


MAX = 2 ** 31 - 1


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        
        l = len(S)
        for i in range(1, l + 1):
            num_str = S[:i]
            if len(num_str) > 1 and num_str.startswith("0"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""t""i""n""u""e""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""u""m"" ""="" ""i""n""t""(""n""u""m""_""s""t""r"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""n""u""m"" "">"" ""M""A""X"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""b""r""e""a""k""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""r""a""n""g""e""(""i"" ""+"" ""1"","" ""l"" ""+"" ""1"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""n""u""m""2""_""s""t""r"" ""="" ""S""[""i"":""j""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""l""e""n""(""n""u""m""2""_""s""t""r"")"" "">"" ""1"" ""a""n""d"" ""n""u""m""2""_""s""t""r"".""s""t""a""r""t""s""w""i""t""h""(