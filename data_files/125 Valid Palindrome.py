
__author__ = 'Danyang'


class Solution(object):
    def isPalindrome(self, s):
        
        s = s.lower()
        
        
        s = ''.join(e for e in s if e.isalnum())
        if not s:
            return True

        return s == s[::-1]