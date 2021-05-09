

from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        
        A.sort()
        mn = min(A)
        mx = max(A)
        ret = mx - mn
        for i in range(len(A) - 1):
            cur_mx = max(mx - K, A[i] + K)
            cur_mn = min(mn + K, A[i+1] - K)
            ret = min(ret, cur_mx - cur_mn)

        return ret

    def smallestRangeII_error(self, A: List[int], K: int) -> int:
        
        mini = min(A)
        maxa = max(A)
        
        B = []
        max_upper_diff = 0
        max_lower_diff = 0
        upper = max(mini + K, maxa - K)  
        lower = min(mini + K, maxa - K)
        for a in A:
            diffs = [(a + K) - upper, lower - (a - K)]
            cur_diff = min(diffs)
            if cur_diff == diffs[0] and cur_diff >= max_upper_diff:
                max_upper_diff = cur_diff
            elif cur_diff == diffs[1] and cur_diff >= max_lower_diff:
                max_lower_diff = cur_diff

        return upper + max_upper_diff - (lower + max_lower_diff)
