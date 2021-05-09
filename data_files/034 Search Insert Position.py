
__author__ = 'Danyang'
class Solution:
    def searchInsert_complex(self, A, target):
        
        length = len(A)
        if not A or length==0:
            return 0

        start = 0
        end = length -1
        
        while True:
            mid = (start+end)/2
            if target==A[mid]:
                return mid
            elif target<A[mid]:
                end = mid-1
                if not start<=end:
                    
                    return mid if mid>=0 else 0
            else:
                start = mid+1
                if not start<=end:
                    return start

    def searchInsert(self, A, target):
        
        length = len(A)
        if not A or length==0:
            return 0

        start = 0
        end = length
        while start<end:
            mid = (start + end) / 2
            if target==A[mid]:
                return mid
            elif target<A[mid]:
                end = mid
            else:
                start = mid + 1

        return start

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""e""a""r""c""h""I""n""s""e""r""t""(""[""1"","" ""3"","" ""5"","" ""6""]"","" ""5"")""=""=""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""e""a""r""c""h""I""n""s""e""r""t""(""[""1"","" ""3"","" ""5"","" ""6""]"","" ""2"")""=""=""1""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""e""a""r""c""h""I""n""s""e""r""t""(""[""1"","" ""3"","" ""5"","" ""6""]"","" ""7"")""=""=""4""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""e""a""r""c""h""I""n""s""e""r""t""(""[""1"","" ""3"","" ""5"","" ""6""]"","" ""0"")""=""=""0""
""
""
""
