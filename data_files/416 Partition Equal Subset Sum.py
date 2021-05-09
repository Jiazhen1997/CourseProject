

from collections import defaultdict


class Solution:
    def canPartition(self, nums):
        
        if not nums:
            return False

        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2
        d = defaultdict(lambda: defaultdict(int))
        d[0][0] = 1
        d[0][nums[0]] = 1

        for i in range(1, len(nums)):
            for v in range(target + 1):
                d[i][v] = d[i-1][v] + d[i-1][v-nums[i]]

        return any(d[i][target] > 0 for i in range(len(nums)))

    def canPartition_TLE(self, nums):
        
        nums.sort()
        s = sum(nums)
        if s % 2 != 0:
            return False

        target = s // 2
        return self.dfs(nums, 0, target)

    def dfs(self, nums, idx, target):
        
        if not idx < len(nums):
            return False
        if nums[idx] == target:
            return True
        if nums[idx] > target:
            return False

        return (
            self.dfs(nums, idx + 1, target) or   
            self.dfs(nums, idx + 1, target - nums[idx])  
        )


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""P""a""r""t""i""t""i""o""n""(""[""1"","" ""5"","" ""1""1"","" ""5""]"")"" ""=""="" ""T""r""u""e""
"" "" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""P""a""r""t""i""t""i""o""n""(""[""1"","" ""2"","" ""3"","" ""5""]"")"" ""=""="" ""F""a""l""s""e""
