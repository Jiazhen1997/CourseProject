
__author__ = 'Daniel'


class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        
        S_A = (C-A)*(D-B)
        S_B = (G-E)*(H-F)

        l = max(0, min(C, G)-max(A, E))
        h = max(0, min(D, H)-max(B, F))
        return S_A + S_B - l*h


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""m""p""u""t""e""A""r""e""a""(""-""2"","" ""-""2"","" ""2"","" ""2"","" ""-""2"","" ""-""2"","" ""2"","" ""2"")"" ""=""="" ""1""6