

from collections import defaultdict


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        F = defaultdict(lambda: defaultdict(int))
        m = len(word1)
        n = len(word2)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    F[i][j] = F[i-1][j-1] + 1
                else:
                    F[i][j] = max(
                        F[i-1][j],
                        F[i][j-1],
                    )

        return m - F[m][n] + n - F[m][n]

    def minDistance_edit_distance(self, word1: str, word2: str) -> int:
        
        F = defaultdict(lambda: defaultdict(int))
        m = len(word1)
        n = len(word2)

        
        for i in range(1, m + 1):
            F[i][0] = i
        for j in range(1, n + 1):
            F[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    F[i][j] = F[i-1][j-1]
                else:
                    F[i][j] = min(
                        F[i-1][j] + 1,
                        F[i][j-1] + 1,
                    )

        return F[m][n]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""D""i""s""t""a""n""c""e""(