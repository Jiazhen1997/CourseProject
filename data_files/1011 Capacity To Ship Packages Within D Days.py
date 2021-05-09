

from tying import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        
        lo = max(weights)
        hi = sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            cnt = 1
            cur = 0
            for w in weights:
                cur += w
                if cur > mid:
                    cnt += 1
                    cur = w
                    
            if cnt > D:
                lo = mid + 1
            else:
                hi = mid

        return lo
