

from typing import List


class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        
        for _ in range(V):
            s = K
            
            optimal = s
            for i in range(s-1, -1, -1):
                if heights[i] <= heights[i+1]:
                    if heights[i] < heights[optimal]:
                        optimal = i
                else:
                    break
            if optimal == s:
                
                for i in range(s+1, len(heights)):
                    if heights[i] <= heights[i-1]:
                        if heights[i] < heights[optimal]:
                            optimal = i
                    else:
                        break
            heights[optimal] += 1

        return heights


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""p""o""u""r""W""a""t""e""r""(""[""2"",""1"",""1"",""2"",""1"",""2"",""2""]"","" ""4"","" ""3"")"" ""=""="" ""[""2"",""2"",""2"",""3"",""2"",""2"",""2""]""
