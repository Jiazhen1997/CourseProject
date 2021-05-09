
__author__ = 'Daniel'


class Solution(object):
    def removeKdigits(self, num, k):
        
        stk = []  
        for char in num:
            while k and stk and stk[-1] > char:
                stk.pop()
                k -= 1

            stk.append(char)

        for _ in xrange(k): stk.pop()

        return ''.join(stk).lstrip('0') or '0'
