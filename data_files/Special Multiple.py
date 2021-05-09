
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        N = cipher

        x = 1
        while True:  
            binary = bin(x)[2:]
            nine_ary = str(binary).replace("1"","" 