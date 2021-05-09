



class Solution:
    def findDiagonalOrder(self, matrix):
        
        if not matrix:
            return []

        R, C = len(matrix), len(matrix[0])
        F = [[] for _ in range(R+C-1)]
        for r in range(R):
            for c in range(C):
                F[r+c].append(matrix[r][c])

        ret = []
        for i in range(R+C-1):
            if i % 2 == 1:
                ret.extend(F[i])
            else:
                ret.extend(F[i][::-1])

        return ret

    def findDiagonalOrder_2(self, matrix):
        
        if not matrix:
            return []
        i = 0
        j = 0
        inc = True
        ret = []
        R, C = len(matrix), len(matrix[0])
        while True:
            ret.append(matrix[i][j])
            if i == R - 1 and j == C - 1:
                break
            if inc:
                i -= 1
                j += 1
                if i < 0 or j >= C:
                    inc = False
                    if i < 0 and j < C:
                        i = 0
                    else:
                        i += 2
                        j = C - 1
            else:
                i += 1
                j -= 1
                if i >= R or j < 0:
                    inc = True
                    if j < 0 and i < R:
                        j = 0
                    else:
                        i = R - 1
                        j += 2

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""D""i""a""g""o""n""a""l""O""r""d""e""r""(""[""
"" "" "" "" "" "" "" "" ""["" ""1"","" ""2"","" ""3"" ""]"",""
"" "" "" "" "" "" "" "" ""["" ""4"","" ""5"","" ""6"" ""]"",""
"" "" "" "" "" "" "" "" ""["" ""7"","" ""8"","" ""9"" ""]""
"" "" "" "" ""]"")"" ""=""="" ""[""1"",""2"",""4"",""7"",""5"",""3"",""6"",""8"",""9""]""
