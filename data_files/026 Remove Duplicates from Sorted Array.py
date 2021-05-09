
__author__ = 'Danyang'
class Solution:
    def removeDuplicates(self, A):
        
        length = len(A)

        
        if length==0 or length==1:
            return length

        
        closed_ptr = 0
        open_ptr = 1
        while open_ptr<length:
            
            if A[closed_ptr]==A[open_ptr]:
                open_ptr += 1
                continue  

            non_duplicate = A[open_ptr]
            A[closed_ptr+1] = non_duplicate
            closed_ptr += 1

        return closed_ptr+1 

    def removeDuplicates_another_loop_style(self, A):
        
        length = len(A)

        if length==0 or length==1:
            return length

        closed_ptr = 0
        open_ptr = 1
        while open_ptr<length:
            while open_ptr<length and A[closed_ptr]==A[open_ptr]:
                open_ptr += 1

            if open_ptr<length:
                non_duplicate = A[open_ptr]
                A[closed_ptr+1] = non_duplicate
                closed_ptr += 1

        return closed_ptr+1 