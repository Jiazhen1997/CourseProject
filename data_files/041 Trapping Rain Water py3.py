


class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)
        lefts = [0 for _ in range(n+1)]
        rights = [0 for _ in range(n+1)]
        for i in range(1, n+1):  
            lefts[i] = max(lefts[i-1], height[i-1])
        for i in range(n-1, -1, -1):
            rights[i] = max(rights[i+1], height[i])

        ret = 0
        for i in range(n):
            ret += max(
                0,
                min(lefts[i], rights[i+1]) - height[i]
            )
        return ret
