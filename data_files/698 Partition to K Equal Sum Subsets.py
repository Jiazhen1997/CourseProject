

from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        s = sum(nums)
        if s % k != 0:
            return False

        target = s // k
        visited = [False for _ in nums]
        return self.dfs(nums, 0, None, target, visited, k)

    def dfs(self, nums, start_idx, cur_sum, target_sum, visited, k):
        
        if k == 1:
            return True

        if cur_sum and cur_sum == target_sum:
            
            return self.dfs(nums, 0, None, target_sum, visited, k - 1)

        for i in range(start_idx, len(nums)):
            if not visited[i]:
                
                visited[i] = True
                nxt_sum = (cur_sum or 0) + nums[i]
                
                
                if self.dfs(nums, i + 1, nxt_sum, target_sum, visited, k):
                    return True
                visited[i] = False

        return False


class Solution_TLE:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        s = sum(nums)
        if s % k != 0:
            return False

        target = s // k
        visited = [False for _ in nums]
        return self.dfs(nums, None, target, visited, k)

    def dfs(self, nums, cur_sum, target_sum, visited, k):
        
        if k == 0:
            return True

        if cur_sum and cur_sum == target_sum:
            return self.dfs(nums, None, target_sum, visited, k - 1)

        for i in range(len(nums)):
            if not visited[i]:
                
                visited[i] = True
                nxt_sum = (cur_sum or 0) + nums[i]
                
                
                if self.dfs(nums, nxt_sum, target_sum, visited, k):
                    return True
                visited[i] = False

        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""P""a""r""t""i""t""i""o""n""K""S""u""b""s""e""t""s""(""[""5"","" ""3"","" ""2"","" ""3"","" ""1"","" ""2"","" ""4""]"","" ""4"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""P""a""r""t""i""t""i""o""n""K""S""u""b""s""e""t""s""(""[""4"","" ""3"","" ""2"","" ""3"","" ""5"","" ""2"","" ""1""]"","" ""4"")"" ""=""="" ""T""r""u""e""
