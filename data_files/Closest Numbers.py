
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N, A = cipher
        A.sort()

        diff = 1 << 31
        lst = []
        for i in xrange(N - 1):
            b = A[i + 1]
            a = A[i]
            if abs(a - b) < diff:
                diff = abs(a - b)
                lst = [a, b]
            elif abs(a - b) == diff:
                lst.append(a)
                lst.append(b)

        return " "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""l""s""t"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 