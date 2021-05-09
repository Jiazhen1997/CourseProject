
__author__ = 'Danyang'
class Solution:
    def subsets(self, S):
        
        S.sort()
        result = []
        self.generate_subsets(S, [], result)
        return result

    def generate_subsets(self, S, current, result):
        result.append(current)
        for ind, val in enumerate(S):
            self.generate_subsets(S[ind+1:], current+[val], result)

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""s""u""b""s""e""t""s""(""[""1"","" ""2"","" ""3""]"")