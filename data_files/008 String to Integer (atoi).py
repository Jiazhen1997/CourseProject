
__author__ = 'Danyang'


class Solution:
    def atoi(self, str):
        
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        str = str.strip()
        if not str:
            return 0

        
        sign = 1
        if str[0] in ("+"","" 