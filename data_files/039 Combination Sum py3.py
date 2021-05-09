

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(candidates, 0, [], 0, target, ret)
        return ret

    def dfs(self, candidates, i, cur, cur_sum, target, ret):
        if cur_sum == target:
            ret.append(list(cur))
            return
            
        if cur_sum > target or i >= len(candidates):
            return

        
        self.dfs(candidates, i + 1, cur, cur_sum, target, ret)

        
        cur.append(candidates[i])
        cur_sum += candidates[i]
        self.dfs(candidates, i, cur, cur_sum, target, ret)
        cur.pop()
        cur_sum -= candidates[i]
