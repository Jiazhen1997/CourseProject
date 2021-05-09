

from typing import List
from collections import defaultdict


class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        
        if not nums:
            return

        counter = defaultdict(int)
        first = {}  
        mx = [0, 0]  
        for i, n in enumerate(nums):
            if n not in first:
                first[n] = i  
            counter[n] += 1
            if counter[n] > mx[0]:
                
                mx = [counter[n], i - first[n] + 1]
            elif counter[n] == mx[0]:
                
                mx[1] = min(mx[1], i - first[n] + 1)

        return mx[1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""S""h""o""r""t""e""s""t""S""u""b""A""r""r""a""y""(""[""1"","" ""2"","" ""2"","" ""3"","" ""1""]"")"" ""=""="" ""2""
