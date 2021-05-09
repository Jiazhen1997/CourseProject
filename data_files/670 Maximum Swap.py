



class Solution:
    def maximumSwap(self, num: int) -> int:
        
        stk = []
        nums = list(str(num))
        n = len(nums)
        for i in range(n-1, -1, -1):
            if stk and stk[-1][1] >= nums[i]:  
                continue
            stk.append((i, nums[i]))

        for i in range(n):
            while stk and stk[-1][0] <= i:
                stk.pop()
            if stk and stk[-1][1] > nums[i]:
                j = stk[-1][0]
                nums[i], nums[j] = nums[j], nums[i]
                break

        return int("".""j""o""i""n""(""n""u""m""s"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 