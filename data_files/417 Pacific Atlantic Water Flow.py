

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))


class Solution:
    def pacificAtlantic(self, matrix):
        
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])  
        
        P = [[False for _ in range(n)] for _ in range(m)]
        A = [[False for _ in range(n)] for _ in range(m)]

        
        for i in range(m):
            self.dfs(matrix, i, 0, P)
            self.dfs(matrix, i, n-1, A)

        for j in range(n):
            self.dfs(matrix, 0, j, P)
            self.dfs(matrix, m-1, j, A)

        ret = [
            [i, j]
            for i in range(m)
            for j in range(n)
            if P[i][j] and A[i][j]
        ]
        return ret

    def dfs(self, matrix, i, j, C):
        
        C[i][j] = True
        m, n = len(matrix), len(matrix[0])
        for x, y in dirs:
            I = i + x
            J = j + y
            if 0 <= I < m and 0 <= J < n and matrix[i][j] <= matrix[I][J]:
                if not C[I][J]:
                    self.dfs(matrix, I, J, C)


    def pacificAtlantic_error(self, matrix):
        
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])  
        P = [[False] * n ] * m
        A = [[False] * n ] * m

        visisted = [[False] * n ] * m
        for i in range(m):
            for j in range(n):
                self.dfs_error(matrix, i, j, visisted, P, lambda i, j: i < 0 or j <0)

        visisted = [[False] * n ] * m
        for i in range(m):
            for j in range(n):
                self.dfs_error(matrix, i, j, visisted, A, lambda i, j: i >= m or j >= n)

        ret = [
            [i, j]
            for i in range(m)
            for j in range(n)
            if P[i][j] and A[i][j]
        ]
        return ret


    def dfs_error(self, matrix, i, j, visisted, C, predicate):
        m, n = len(matrix), len(matrix[0])
        if visisted[i][j]:
            return C[i][j]

        visisted[i][j] = True
        for x, y in dirs:
            i2 = i + x
            j2= j + y
            if 0 <= i2 < m and 0 <= j2 < n:
                if self.dfs_error(matrix, i2, j2, visisted, C, predicate) and matrix[i][j] >= matrix[i2][j2]:
                    C[i][j] = True
            elif predicate(i2, j2):
                C[i][j] = True

        return C[i][j]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""a""c""i""f""i""c""A""t""l""a""n""t""i""c""(""[""
"" "" "" "" "" "" "" "" ""[""1"",""2"",""2"",""3"",""5""]"",""
"" "" "" "" "" "" "" "" ""[""3"",""2"",""3"",""4"",""4""]"",""
"" "" "" "" "" "" "" "" ""[""2"",""4"",""5"",""3"",""1""]"",""
"" "" "" "" "" "" "" "" ""[""6"",""7"",""1"",""4"",""5""]"",""
"" "" "" "" "" "" "" "" ""[""5"",""1"",""1"",""2"",""4""]""
"" "" "" "" ""]"")"" ""=""="" ""[""[""0"","" ""4""]"","" ""[""1"","" ""3""]"","" ""[""1"","" ""4""]"","" ""[""2"","" ""2""]"","" ""[""3"","" ""0""]"","" ""[""3"","" ""1""]"","" ""[""4"","" ""0""]""]""
