
__author__ = 'Danyang'


class Solution:
    def reverseWords(self, s):
        
        words_lst = s.split()  
        words_lst = reversed(words_lst)
        return ' '.join(words_lst)