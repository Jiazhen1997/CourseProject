



class Solution:
    def nextGreaterElement(self, nums1, nums2):
        
        h = {}  
        stk = []
        for e in nums2[::-1]:
            while stk and stk[-1] <= e:
                
                stk.pop()

            h[e] = stk[-1] if stk else -1
            stk.append(e)

        return [
            h[q]
            for q in nums1
        ]
