
import sys

__author__ = 'Daniel'


class Solution:
    def findPeakII(self, A):
        
        minint = -sys.maxint-1

        left = 0
        right = len(A[0])
        top = 0
        bottom = len(A)

        while left < right and top < bottom:
            if right-left > bottom-top:
                mid = (right+left)/2
                l_max = minint  
                r_max = minint  
                c_max = minint  
                c_i, c_j = -1, -1  
                for i in xrange(top, bottom):
                    l_max = max(l_max, A[i][mid-1])
                    r_max = max(r_max, A[i][mid+1])
                    c_max = max(c_max, A[i][mid])
                    if c_max == A[i][mid]:
                        c_i, c_j = i, mid

                if l_max > c_max and l_max > r_max:
                    right = mid
                elif r_max > c_max and r_max > l_max:
                    left = mid+1
                else:
                    return [c_i, c_j]

            else:
                mid = (top+bottom)/2
                u_max = minint  
                d_max = minint  
                c_max = minint  
                c_i, c_j = -1, -1
                for j in xrange(left, right):
                    u_max = max(u_max, A[mid-1][j])
                    d_max = max(d_max, A[mid+1][j])
                    c_max = max(c_max, A[mid][j])
                    if c_max == A[mid][j]:
                        c_i, c_j = mid, j

                if u_max > c_max and u_max > d_max:
                    bottom = mid
                elif d_max > c_max and d_max > u_max:
                    top = mid+1
                else:
                    return [c_i, c_j]

        return [-1, -1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""A"" ""="" ""[""
"" "" "" "" "" "" "" "" ""[""1"","" "" ""2"","" "" ""3"","" "" ""4"","" "" "" ""5"","" ""6""]"",""
"" "" "" "" "" "" "" "" ""[""1""4"","" ""1""5"","" ""1""6"","" ""1""7"","" ""1""8"","" ""8""]"",""
"" "" "" "" "" "" "" "" ""[""1""2"","" ""1""3"","" ""1""1"","" ""1""0"","" "" ""9"","" ""7""]""
"" "" "" "" ""]""
""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""P""e""a""k""I""I""(""A"")