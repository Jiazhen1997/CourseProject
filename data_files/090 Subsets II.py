
__author__ = 'Danyang'
class Solution:
    def subsetsWithDup(self, S):
        
        S.sort()
        result = []
        self.get_subset(S, [], result)
        return result

    def get_subset(self, S, current, result):
        result.append(current)
        for ind, val in enumerate(S):
            
            if ind-1>=0 and val==S[ind-1]:  
                continue
            self.get_subset(S[ind+1:], current+[val], result)


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""s""u""b""s""e""t""s""W""i""t""h""D""u""p""(""[""1"","" ""2"","" ""3""]"")