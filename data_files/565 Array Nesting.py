

from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        
        visited = set()
        ret = 0
        for n in nums:
            count = self.dfs(nums, n, set(), visited)
            ret = max(ret, count)

        return ret

    def dfs(self, nums, num, path, visited):
        if num in visited:
            return 0

        visited.add(num)
        path.add(num)  
        self.dfs(nums, nums[num], path, visited)
        return len(path)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""a""r""r""a""y""N""e""s""t""i""n""g""(""[""5"",""4"",""0"",""3"",""1"",""6"",""2""]"")"" ""=""="" ""4""
