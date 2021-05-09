
__author__ = 'Danyang'
class Solution:
    def trap(self, A):
        
        left_maxs = [0 for _ in A]  
        right_maxs = [0 for _ in A]  

        left_max = 0
        for ind, val in enumerate(A):
            left_max = max(left_max, val)
            left_maxs[ind] = left_max

        right_max = 0
        
        for ind, val in reversed(list(enumerate(A))):
            right_max = max(right_max, val)
            right_maxs[ind] = right_max

        
        volume = 0
        for ind, val in enumerate(A):
            volume += max(0, min(left_maxs[ind], right_maxs[ind]) - val)

        return volume


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""t""r""a""p""(""[""0"","" ""1"","" ""0"","" ""2"","" ""1"","" ""0"","" ""1"","" ""3"","" ""2"","" ""1"","" ""2"","" ""1""]"")""
""
""
""
""
