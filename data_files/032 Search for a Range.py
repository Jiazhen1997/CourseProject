

__author__ = 'Danyang'
class Solution:
    def searchRange(self, A, target):
        
        result = []
        length = len(A)

        
        start = 0
        end = length  
        while start<end:
            mid = (start+end)/2
            if A[mid]<target:  
                start = mid+1
            else:
                end = mid

        if start<length and A[start]==target:
            result.append(start)
        else:
            return [-1, -1]

        
        start = start
        end = length  
        while start<end:
            mid = (start+end)/2
            if A[mid]<=target:  
                start = mid+1
            else:
                end = mid

        result.append(start-1)
        return result