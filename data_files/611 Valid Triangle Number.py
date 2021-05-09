

from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        ret = 0
        nums.sort()
        n = len(nums)
        for k in range(n-1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ret += j - i  
                    j -= 1  
                else:
                    i += 1  

        return ret

    def triangleNumber_error(self, nums: List[int]) -> int:
        
        ret = 0
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                
                if nums[i] + nums[j] > nums[k]:
                    ret += k - j
                    k -= 1
                else:
                    j += 1

        return ret

    def triangleNumber_slow(self, nums: List[int]) -> int:
        
        cache = {}
        nums.sort()
        n = len(nums)
        ret = 0
        for i in range(n):
            for j in range(i + 1, n):
                if (i, j) not in cache:
                    cur = 0
                    for k in range(j + 1, n):
                        if nums[k] < nums[i] + nums[j]:
                            cur += 1
                        else:
                            break
                    cache[(i, j)] = cur
                ret += cache[(i, j)]

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""t""r""i""a""n""g""l""e""N""u""m""b""e""r""(""[""2"",""2"",""3"",""4""]"")"" ""=""="" ""3""
