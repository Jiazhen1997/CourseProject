
__author__ = 'Danyang'
class Solution:
    def search(self, A, target):
        

        length = len(A)
        start = 0
        end = length-1  
        while start<=end:
            mid = (start+end)/2
            
            if A[mid]==target:
                return mid
            
            if A[start]<A[mid]<A[end]:
                if target>A[mid]:
                    start = mid+1
                else:
                    end = mid-1
            
            elif A[start]>A[mid] and A[mid]<A[end]:
                if target>A[mid] and target<=A[end]:
                    start = mid+1
                else:
                    end = mid -1
            
            else:
                if target<A[mid] and target>=A[start]:
                    end = mid-1
                else:
                    start = mid+1

        return -1

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""s""e""a""r""c""h""(""[""5"",""1"",""3""]"","" ""5"")