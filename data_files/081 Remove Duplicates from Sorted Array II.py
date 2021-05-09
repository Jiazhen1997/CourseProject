
__author__ = 'Danyang'
class Solution:
    def removeDuplicates_complicated(self, A):
        
        length = len(A)
        if length<=2:
            return length

        closed_ptr = 0
        duplicate_count = 0
        open_ptr = closed_ptr+1
        while open_ptr<length:
            if A[closed_ptr]==A[open_ptr]:
                if duplicate_count>=1:
                    
                    try:
                        while A[closed_ptr]==A[open_ptr]:
                            open_ptr+=1
                        duplicate_count = 0
                    except IndexError:
                        break

                
                else:
                    duplicate_count +=1
            else:
                duplicate_count = 0

            A[closed_ptr+1] = A[open_ptr]
            closed_ptr += 1
            open_ptr += 1

        return closed_ptr+1  

    def removeDuplicates(self, A):
        
        length = len(A)
        if length<=2:
            return length

        close_ptr = 0
        duplicate_once = False  
        for open_ptr in range(close_ptr+1, length):
            if A[close_ptr]!=A[open_ptr]:  
                duplicate_once = False
                close_ptr += 1
                A[close_ptr] = A[open_ptr]
            elif not duplicate_once:  
                duplicate_once = True
                close_ptr += 1
                A[close_ptr] = A[open_ptr]
            else:  
                continue  

        return close_ptr+1





if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""r""e""m""o""v""e""D""u""p""l""i""c""a""t""e""s""(""[""1"","" ""1"","" ""2"","" ""2""]"")