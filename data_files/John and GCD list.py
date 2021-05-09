

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = cipher
        B = []
        B.append(A[0])
        for i in xrange(1, len(A)):
            B.append(A[i] * A[i - 1] / self.gcd(A[i], A[i - 1]))
        B.append(A[-1])

        return " "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""B"")"")""
""
"" "" "" "" ""d""e""f"" ""g""c""d""(""s""e""l""f"","" ""a"","" ""b"")"":""
"" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""b"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""a"","" ""b"" ""="" ""b"","" ""a"" ""%"" ""b""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""a""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 