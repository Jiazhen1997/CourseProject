



class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        m, n = len(s1), len(s2)
        F = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        F[0][0] = 0
        for i in range(1, m + 1):
            F[i][0] = F[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            F[0][j] = F[0][j-1] + ord(s2[j-1])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                F[i][j] = min(
                    F[i][j],
                    F[i][j-1] + ord(s2[j-1]),
                    F[i-1][j] + ord(s1[i-1]),
                )
                if s1[i-1] == s2[j-1]:
                    F[i][j] = min(
                        F[i][j],
                        F[i-1][j-1],
                    )

        return F[m][n]

    def minimumDeleteSum_error(self, s1: str, s2: str) -> int:
        
        m, n = len(s1), len(s2)
        F = [[float('inf') for _ in range(n + 1)] for _ in range(m + 1)]
        F[0][0] = 0
        F[1][0] = ord(s1[0])
        F[0][1] = ord(s2[0])
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                F[i][j] = min(
                    F[i][j],
                    F[i][j-1] + ord(s2[j-1]),
                    F[i-1][j] + ord(s1[i-1]),
                )
                if s1[i-1] == s2[j-1]:
                    F[i][j] = min(
                        F[i][j],
                        F[i-1][j-1],
                    )

        return F[m][n]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""i""m""u""m""D""e""l""e""t""e""S""u""m""(