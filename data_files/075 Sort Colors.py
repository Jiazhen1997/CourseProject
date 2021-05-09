
__author__ = 'Danyang'
class Solution:
    def sortColors(self, A):
        
        RED, WHITE, BLUE = 0, 1, 2
        red_end_ptr = -1
        blue_start_ptr= len(A)

        i = 0
        while i<blue_start_ptr:
            if A[i]==WHITE: 
                i += 1
            elif A[i]==RED:
                red_end_ptr+=1
                A[red_end_ptr], A[i] = A[i], A[red_end_ptr]
                i += 1
            else:
                blue_start_ptr -= 1
                A[blue_start_ptr], A[i] = A[i], A[blue_start_ptr]
                

        

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""s""o""r""t""C""o""l""o""r""s""(""[""1"","" ""2"","" ""0""]"")