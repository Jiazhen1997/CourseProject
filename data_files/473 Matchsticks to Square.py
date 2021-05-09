



class Solution:
    def makesquare(self, nums):
        
        if not nums:
            return False

        square = [0 for _ in range(4)]
        l = sum(nums) // 4
        if sum(nums) % 4 != 0:
            return False

        nums.sort(reverse=True)
        return self.dfs(nums, 0, l, square)

    def dfs(self, nums, i, l, square):
        if i >= len(nums):
            return True

        for j in range(len(square)):
            if nums[i] + square[j] <= l:
                square[j] += nums[i]
                if self.dfs(nums, i + 1, l, square):
                    return True
                square[j] -= nums[i]

        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""k""e""s""q""u""a""r""e""(""[""1"",""1"",""2"",""2"",""2""]"")"" ""=""="" ""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""k""e""s""q""u""a""r""e""(""[""3"",""3"",""3"",""3"",""4""]"")"" ""=""="" ""F""a""l""s""e""
