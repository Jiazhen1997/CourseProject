

from collections import defaultdict


class Solution:
    def longestPalindromeSubseq(self, s):
        
        n = len(s)
        F = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            F[i][i] = 1

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                F[i][j] = max(F[i+1][j], F[i][j-1])
                if s[i] == s[j]:
                    F[i][j] = max(F[i][j], F[i+1][j-1] + 2)

        return F[0][n-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""o""n""g""e""s""t""P""a""l""i""n""d""r""o""m""e""S""u""b""s""e""q""(