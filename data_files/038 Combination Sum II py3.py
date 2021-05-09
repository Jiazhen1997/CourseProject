

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        self.dfs(candidates, 0, [], 0, target, ret)
        return ret

    def dfs(self, candidates, i, cur, cur_sum, target, ret):
        if cur_sum == target:
            ret.append(list(cur))
            return

        if cur_sum > target or i >= len(candidates):
            return

        
        
        j = i + 1
        while j < len(candidates) and candidates[j] == candidates[i]:
            j += 1

        self.dfs(candidates, j, cur, cur_sum, target, ret)

        
        cur.append(candidates[i])
        cur_sum += candidates[i]
        self.dfs(candidates, i + 1, cur, cur_sum, target, ret)
        cur.pop()
        cur_sum -= candidates[i]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""m""b""i""n""a""t""i""o""n""S""u""m""2""(""[""2"",""5"",""2"",""1"",""2""]"","" ""5"")"" ""=""="" ""[""[""5""]"","" ""[""1"",""2"",""2""]""]""
