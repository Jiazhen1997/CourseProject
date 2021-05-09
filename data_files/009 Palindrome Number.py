
__author__ = 'Danyang'


class Solution:
    def isPalindrome(self, x):
        
        if x < 0:
            return False

        
        div = 1
        while x/div >= 10:
            div *= 10  

        while x > 0:
            msb = x/div
            lsb = x%10

            if msb != lsb:
                return False

            
            x %= div
            x /= 10

            div /= 100

        return True


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""i""s""P""a""l""i""n""d""r""o""m""e""(""2""1""4""7""4""8""3""6""4""7"")