
MOD = 10 ** 9
__author__ = 'Danyang'


class Solution(object):
    def solve(self, n):
        
        result = []

        comb = 1  
        result.append(comb)
        for i in xrange(1, n + 1):
            comb = comb * (n + 1 - i) / i
            result.append(comb % MOD)

        return " "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""s""u""l""t"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 