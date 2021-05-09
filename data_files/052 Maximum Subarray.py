
__author__ = 'Danyang'
class Solution:
    def maxSubArray(self, A):
        
        
        if not A:
            return 0

        
        largest = max(A)
        if largest<0:
            return largest

        max_result = -1<<31
        current_max = 0
        for i in range(len(A)):
            if current_max+A[i]>=0:
                current_max+=A[i]
            else:
                current_max = 0
            max_result = max(max_result, current_max)

        return max_result