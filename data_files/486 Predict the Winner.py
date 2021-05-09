

from collections import defaultdict


class Solution:
    def PredictTheWinner(self, nums):
        
        l = len(nums)
        gross = [0]  
        for e in nums:
            gross.append(gross[-1] + e)

        F = defaultdict(lambda: defaultdict(int))
        for i in range(l-1, -1, -1):
            for j in range(i+1, l+1):
                F[i][j] = max(
                    gross[j] - gross[i] - F[i+1][j],
                    gross[j] - gross[i] - F[i][j-1]
                )
        return F[0][l] >= (gross[-1] - F[0][l])


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""P""r""e""d""i""c""t""T""h""e""W""i""n""n""e""r""(""[""1"","" ""5"","" ""2""]"")"" ""=""="" ""F""a""l""s""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""P""r""e""d""i""c""t""T""h""e""W""i""n""n""e""r""(""[""1"","" ""5"","" ""2""3""3"","" ""7""]"")"" ""=""="" ""T""r""u""e""
