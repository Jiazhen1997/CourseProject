
__author__ = 'Danyang'


class Solution:
    def findMedianSortedArrays(self, A, B):
        
        m = len(A)
        n = len(B)
        if ((m+n)&1 == 0):
            return (self.find_kth(A, B, (m+n)/2)+self.find_kth(A, B, (m+n)/2-1))/2.0
        else:
            return self.find_kth(A, B, (m+n)/2)

    def find_kth(self, A, B, k):
        
        if not A:  return B[k]
        if not B:  return A[k]
        if k == 0: return min(A[0], B[0])

        m, n = len(A), len(B)
        
        if A[m/2] >= B[n/2]:
            if k > m/2+n/2:
                return self.find_kth(A, B[n/2+1:], k-n/2-1)  
            else:
                return self.find_kth(A[:m/2], B, k)  
        else:
            return self.find_kth(B, A, k)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""e""d""i""a""n""S""o""r""t""e""d""A""r""r""a""y""s""(""[""1"","" ""2""]"","" ""[""1"","" ""2"","" ""3""]"")"" ""=""="" ""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""e""d""i""a""n""S""o""r""t""e""d""A""r""r""a""y""s""(""[""1"","" ""2""]"","" ""[""3""]"")"" ""=""="" ""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""e""d""i""a""n""S""o""r""t""e""d""A""r""r""a""y""s""(""[""1""]"","" ""[""2"","" ""3""]"")"" ""=""="" ""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""M""e""d""i""a""n""S""o""r""t""e""d""A""r""r""a""y""s""(""[""1"","" ""2""]"","" ""[""1"","" ""2""]"")"" ""=""="" ""1"".""5""
