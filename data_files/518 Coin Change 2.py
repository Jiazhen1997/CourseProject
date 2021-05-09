

from collections import defaultdict


class Solution:
    def change(self, amount, coins):
        
        F = defaultdict(lambda: defaultdict(int))
        n = len(coins)
        for l in range(n + 1):
            F[0][l] = 1   
             

        for a in range(1, amount + 1):
            for l in range(1, n + 1):
                F[a][l] = F[a][l-1] + F[a - coins[l-1]][l]

        return F[amount][n]


    def change_TLE(self, amount, coins):
        
        if amount == 0:
            return 1

        coins.sort()
        n = len(coins)
        F = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            F[coins[i]][i] = 1

        for a in range(1, amount + 1):
            for i in range(n):
                for j in range(i + 1):
                    F[a][i] += F[a - coins[i]][j]

        return sum(F[amount].values())

    def change_error(self, amount, coins):
        
        F = {0: 1}
        for a in range(1, amount + 1):
            F[a] = 0
            for c in coins:
                if a - c in F:
                    F[a] += F[a - c]

        return F[amount]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""h""a""n""g""e""(""5"","" ""[""1"","" ""2"","" ""5""]"")"" ""=""="" ""4""
