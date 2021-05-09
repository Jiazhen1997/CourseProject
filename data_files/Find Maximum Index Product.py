

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        A = cipher
        L = [-1 for _ in A]
        for i in xrange(1, len(A)):
            idx = i - 1
            while idx != -1:
                if A[idx] > A[i]:
                    L[i] = idx
                    break
                idx = L[idx]

        R = [-1 for _ in A]
        for i in xrange(len(A) - 2, -1, -1):
            idx = i + 1
            while idx != -1:
                if A[idx] > A[i]:
                    R[i] = idx
                    break
                idx = R[idx]

        maxa = -1
        for i in xrange(len(A)):
            left = L[i] + 1
            right = R[i] + 1
            maxa = max(maxa, left * right)

        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(