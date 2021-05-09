
__author__ = 'Danyang'
class Solution:
    def singleNumber(self, A):
        
        storage = 0
        for element in A:
            storage ^= element 

        return storage
