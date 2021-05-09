

from typing import List
from collections import defaultdict


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        rewards = [0 for _ in range(10001)]
        for num in nums:
            rewards[num] += num

        
        cur, prev = 0, 0
        for reward in rewards:
            nxt = max(cur, prev + reward)
            prev = cur
            cur = nxt

        return cur

    def deleteAndEarn_dp(self, nums: List[int]) -> int:
        
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        F = [0 for _ in range(10000 + 3)]
        for i in range(3, 10000 + 3):
            cur = i - 2
            F[i] = max(
                F[i-1],
                F[i-2] + counter[cur] * cur
            )
        return F[-1]

    def deleteAndEarn_slow(self, nums: List[int]) -> int:
        
        nums.sort()
        
        counter = []
        i = 0
        j = 0
        while i < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            counter.append((nums[i], j - i))
            i = j

        
        F = [0 for _ in counter]
        for i in range(len(counter)):
            F[i] = counter[i][0] * counter[i][1]
            F[i] += max(
                [
                    F[j]
                    for j in range(i)
                    if counter[j][0] != counter[i][0] - 1
                ]
                or [0]
            )

        return max(F or [0])


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""d""e""l""e""t""e""A""n""d""E""a""r""n""(""[""1"",""1"",""1"",""2"",""4"",""5"",""5"",""5"",""6""]"")"" ""=""="" ""1""8""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""d""e""l""e""t""e""A""n""d""E""a""r""n""(""[""3"","" ""4"","" ""2""]"")"" ""=""="" ""6""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""d""e""l""e""t""e""A""n""d""E""a""r""n""(""[""2"","" ""2"","" ""3"","" ""3"","" ""3"","" ""4""]"")"" ""=""="" ""9""
