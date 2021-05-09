
__author__ = 'Danyang'


class Solution:
    def maxArea(self, height):
        
        start = 0
        end = len(height)-1

        max_area = -1 << 32
        while start < end:
            area = min(height[start], height[end])*(end-start)
            max_area = max(area, max_area)

            
            
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return max_area

