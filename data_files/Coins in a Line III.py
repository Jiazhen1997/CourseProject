
__author__ = 'Daniel'


class Solution:
    def firstWillWin_MLE(self, values):
        
        n = len(values)
        if n == 1:
            return True

        F = [[[0 for _ in xrange(n)] for _ in xrange(n)] for _ in xrange(2)]
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1]+values[i-1]

        for i in xrange(n):
            for p in xrange(2):
                F[p][i][i] = values[i]

        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1, n):
                for p in xrange(2):
                    F[p][i][j] = max(
                        values[i]+s[j+1]-s[i+1]-F[1^p][i+1][j],
                        values[j]+s[j]-s[i]-F[1^p][i][j-1]
                    )

        return F[0][0][n-1]>min(F[1][0][n-2], F[1][1][n-1])

    def firstWillWinNormalCase(self, values):
        
        n = len(values)
        if n == 1:
            return True

        SZ = 4
        F = [[[0 for _ in xrange(SZ)] for _ in xrange(SZ)] for _ in xrange(2)]
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1]+values[i-1]

        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1, n):
                for p in xrange(2):
                    if j == i+1:
                        a = values[i+1]
                        b = values[i]
                    else:
                        a = F[1^p][(i+1)%SZ][j%SZ]
                        b = F[1^p][i%SZ][(j-1)%SZ]

                    F[p][i%SZ][j%SZ] = max(
                        values[i]+s[j+1]-s[i+1]-a,
                        values[j]+s[j]-s[i]-b
                    )

        return F[0][0][(n-1)%SZ] > min(F[1][0][(n-2)%SZ], F[1][1][(n-1)%SZ])

    def firstWillWin(self, values):
        
        n = len(values)
        if n%2 == 0 and self.firstWillWinEven(values):
            return True

        return self.firstWillWinNormalCase(values)

    def firstWillWinEven(self, values):
        
        odd_s = 0
        even_s = 0
        for i in xrange(len(values)):
            if i%2 == 0:
                even_s += values[i]
            else:
                odd_s += values[i]

        return odd_s != even_s


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""r""s""t""W""i""l""l""W""i""n""(""[""3"","" ""2"","" ""2""]"")"" ""i""s"" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""r""s""t""W""i""l""l""W""i""n""(""[""1"","" ""2""0"","" ""4""]"")"" ""i""s"" ""F""a""l""s""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""r""s""t""W""i""l""l""W""i""n""(""[""1"","" ""2"","" ""3"","" ""4"","" ""5"","" ""6"","" ""7"","" ""8"","" ""1""3"","" ""1""1"","" ""1""0"","" ""9""]"")"" ""i""s"" ""T""r""u""e