



class Solution:
    def minSteps(self, n: int) -> int:
        
        ret = 0
        for i in range(2, n+1):
            while n % i == 0:
                ret += i
                n //= i

        return ret

    def minSteps_dp(self, n: int) -> int:
        
        F = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        F[1][0] = 0
        F[1][1] = 1
        for i in range(2, n + 1):
            for j in range(i+1):
                F[i][j] = min(
                    F[i][j],
                    F[i-j][j] + 1,
                )
                if i % 2 == 0:
                    F[i][i//2] = min(
                        F[i][i//2],
                        F[i//2][j] + 2
                    )


        ret = min(F[n])
        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""S""t""e""p""s""(""7"")"" ""=""="" ""7""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""S""t""e""p""s""(""3"")"" ""=""="" ""3""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""S""t""e""p""s""(""4"")"" ""=""="" ""4""
