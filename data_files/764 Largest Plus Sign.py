

from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        
        G = [[1 for _ in range(N)] for _ in range(N)]
        for i, j in mines:
            G[i][j] = 0

        F = [[[G[i][j] for _ in range(4)] for j in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                if j - 1 >= 0 and G[i][j] == 1:
                    F[i][j][0] = F[i][j-1][0] + 1
                if i - 1 >= 0 and G[i][j] == 1:
                    F[i][j][1] = F[i-1][j][1] + 1

        for i in range(N-1, -1, -1):
            for j in range(N-1, -1, -1):
                if j + 1 < N and G[i][j] == 1:
                    F[i][j][2] = F[i][j+1][2] + 1
                if i + 1 < N and G[i][j] == 1:
                    F[i][j][3] = F[i+1][j][3] + 1

        ret = 0
        for i in range(N):
            for j in range(N):
                ret = max(ret, min(F[i][j]))

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""o""r""d""e""r""O""f""L""a""r""g""e""s""t""P""l""u""s""S""i""g""n""(""5"","" ""[""[""4"","" ""2""]""]"")"" ""=""="" ""2""
