
__author__ = 'Daniel'


class Solution(object):
    def minPatches(self, nums, n):
        
        cnt = 0
        cur_max = 0
        i = 0
        while cur_max < n:
            if i >= len(nums) or cur_max + 1 < nums[i]:
                cur_max += cur_max + 1
                cnt += 1
            else:
                cur_max += nums[i]
                i += 1

        return cnt

    def minPatches2(self, nums, n):
        
        nums = filter(lambda x: x <= n, nums)

        cnt = 0
        cur_max = 0
        for elt in nums:
            while cur_max + 1 < elt:
                cur_max += cur_max + 1
                cnt += 1

            cur_max += elt

        
        while cur_max < n:
            cur_max += cur_max + 1
            cnt += 1

        return cnt


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""i""n""P""a""t""c""h""e""s""(""[""1"","" ""2"","" ""2"","" ""6"","" ""3""4""]"","" ""2""0"")"" ""=""="" ""1