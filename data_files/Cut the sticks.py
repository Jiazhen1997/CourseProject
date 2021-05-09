
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        A.sort()

        result = []
        while A:
            result.append(len(A))
            A = map(lambda x: x - A[0], A)
            A = filter(lambda x: x > 0, A)

        return "\"n"".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""s""u""l""t"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 