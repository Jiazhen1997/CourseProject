

dirs = (
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (-2, -1),
    (-2, 1),
    (2, -1),
    (2, 1),
)


class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        
        q = set([(r, c)])  
        P = [[0 for _ in range(N)] for _ in range(N)]
        P[r][c] = 1  
        k = 0
        while k < K:
            k += 1
            cur_q = set()
            cur_P = [[0 for _ in range(N)] for _ in range(N)]
            for i, j in q:
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < N and 0 <= J < N:
                        cur_q.add((I, J))
                        cur_P[I][J] += P[i][j] * 1 / 8

            q = cur_q
            P = cur_P

        return sum([
            P[i][j]
            for i in range(N)
            for j in range(N)
        ])


    def knightProbability_error(self, N: int, K: int, r: int, c: int) -> float:
        
        q = [(r, c)]  
        P = [[0 for _ in range(N)] for _ in range(N)]
        P[r][c] = 1  
        k = 0
        while k < K:
            k += 1
            cur_q = []
            cur_P = [[0 for _ in range(N)] for _ in range(N)]
            for i, j in q:
                for di, dj in dirs:
                    I = i + di
                    J = j + dj
                    if 0 <= I < N and 0 <= J < N:
                        cur_q.append((I, J))  
                        cur_P[I][J] += P[i][j] * 1 / 8

            q = cur_q
            P = cur_P

        return sum([
            P[i][j]
            for i in range(N)
            for j in range(N)
        ])


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""n""i""g""h""t""P""r""o""b""a""b""i""l""i""t""y""(""3"","" ""2"","" ""0"","" ""0"")"" "" ""=""="" ""0"".""0""6""2""5""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""k""n""i""g""h""t""P""r""o""b""a""b""i""l""i""t""y""(""3"","" ""3"","" ""0"","" ""0"")"" "" ""=""="" ""0"".""0""1""5""6""2""5""
