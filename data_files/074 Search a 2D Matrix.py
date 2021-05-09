
__author__ = 'Danyang'


class Solution(object):
    def searchMatrix(self, mat, target):
        
        if not mat:
            return False

        m = len(mat)
        n = len(mat[0])

        
        lo = 0
        hi = m  
        while lo < hi:
            mid = (lo+hi)/2
            if mat[mid][0] == target:
                return True
            elif mat[mid][0] < target:
                lo = mid+1
            else:
                hi = mid

        lst = mat[lo-1]  

        
        lo = 0
        hi = n  
        while lo < hi:
            mid = (lo+hi)/2
            if lst[mid] == target:
                return True
            elif lst[mid] < target:
                lo = mid+1
            else:
                hi = mid

        return False


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""s""e""a""r""c""h""M""a""t""r""i""x""(""[""[""1""]"","" ""[""3""]""]"","" ""3"")"" ""=""="" ""T""r""u""e