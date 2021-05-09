




def rand7():
    return 0


class Solution:
    def rand10(self):
        
        while True:
            rv1 = rand7()
            rv2 = rand7()
            s = (rv1 - 1) * 7 + (rv2 - 1)  
            if s < 40:   
                return s % 10 + 1  
