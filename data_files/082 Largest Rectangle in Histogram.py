
import sys
__author__ = 'Danyang'


class Solution:
    def largestRectangleArea(self, height):
        
        if not height:
            return 0

        n = len(height)
        gmax = -sys.maxint-1
        inc_stack = []  

        for i in xrange(n):
            while inc_stack and height[inc_stack[-1]] > height[i]:
                last = inc_stack.pop()
                if inc_stack:  
                    area = height[last]*(i-(inc_stack[-1]+1))
                else:
                    area = height[last]*i
                gmax = max(gmax, area)

            inc_stack.append(i)

        
        i = n
        while inc_stack:
            last = inc_stack.pop()
            if inc_stack:
                area = height[last]*(i-(inc_stack[-1]+1))
            else:
                area = height[last]*i
            gmax = max(gmax, area)

        return gmax

    def largestRectangleArea_TLE(self, height):
        
        if not height:
            return 0

        max_area = -1<<32
        for ind, val in enumerate(height):
            min_h = val
            max_area = max(max_area, val*1)
            for j in xrange(ind, -1, -1):
                min_h = min(min_h, height[j])
                current_area = min_h*(ind-j+1)
                max_area = max(max_area, current_area)

        return max_area


    def largestRectangleArea_complex(self, height):
        
        if not height:
            return 0

        global_max = -1<<32
        for ind, val in enumerate(height):
            if ind+1<len(height) and val<=height[ind+1]:  
                continue

            min_h = val
            global_max = max(global_max, min_h*1)
            for j in xrange(ind, -1, -1):  
                min_h = min(min_h, height[j])
                current_area = min_h*(ind-j+1)
                global_max = max(global_max, current_area)

        return global_max


    def largestRectangleArea_error(self, height):
        
        if not height:
            return 0

        length = len(height)
        global_max = -1<<32
        inc_stack = []  

        i = 0
        while i<length:
            if not inc_stack or height[i]>=height[inc_stack[-1]]:
                inc_stack.append(i)
                i += 1
            else:
                last = inc_stack.pop()
                if inc_stack:
                    area = height[last] * (i-last)
                else:
                    area = height[last] * i
                global_max = max(global_max, area)

        
        while inc_stack:
            last = inc_stack.pop()
            if inc_stack:
                area = height[last]*(i-last)
            else:
                area = height[last]*i
            global_max = max(global_max, area)
        return global_max


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""#"" ""h""e""i""g""h""t"" ""="" ""[""2"","" ""1"","" ""2""]""
"" "" "" "" ""h""e""i""g""h""t"" ""="" ""[""4"","" ""2"","" ""0"","" ""3"","" ""2"","" ""5""]""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""a""r""g""e""s""t""R""e""c""t""a""n""g""l""e""A""r""e""a""(""h""e""i""g""h""t"")"" ""=""="" ""S""o""l""u""t""i""o""n""("")"".""l""a""r""g""e""s""t""R""e""c""t""a""n""g""l""e""A""r""e""a""_""c""o""m""p""l""e""x""(""h""e""i""g""h""t"")""
""
""
""
""
