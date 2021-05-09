
__author__ = 'Daniel'


class Solution:
    def isHappy(self, n):
        
        nxt = 0
        appeared = set()
        while True:
            nxt += (n%10)*(n%10)
            n /= 10
            if n == 0:
                if nxt == 1:
                    return True
                if nxt in appeared:
                    return False

                appeared.add(nxt)
                n = nxt
                nxt = 0

