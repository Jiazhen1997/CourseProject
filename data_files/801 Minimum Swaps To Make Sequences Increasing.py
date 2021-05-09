



class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        
        n = len(A)
        F = [[0 for _ in range(n)] for _ in range(2)]
        F[1][0] = 1
        for i in range(1, n):
            if A[i] > max(A[i-1], B[i-1]) and B[i] > max(A[i-1], B[i-1]):
                
                F[0][i] = min(F[0][i-1], F[1][i-1])
                F[1][i] = min(F[0][i-1], F[1][i-1]) + 1
            elif A[i] > A[i-1] and B[i] > B[i-1]:
                
                
                F[0][i] = F[0][i-1]
                F[1][i] = F[1][i-1] + 1
            else:
                
                F[0][i] = F[1][i-1]
                F[1][i] = F[0][i-1] + 1

        return min(F[0][n-1], F[1][n-1])

    def minSwap_error(self, A: List[int], B: List[int]) -> int:
        
        t = 0
        for i in range(1, len(A)):
            if A[i] <= A[i-1] or B[i] <= B[i-1]:
                t += 1
                if t < i + 1 - t:
                    A[i], B[i] = B[i], A[i]
                else:
                    t = i + 1 - t

        return t


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""S""w""a""p""(""[""0"",""4"",""4"",""5"",""9""]"","" ""[""0"",""1"",""6"",""8"",""1""0""]"")""
