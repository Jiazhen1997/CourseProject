
__author__ = 'Daniel'


class Solution:
    def countDigitOne(self, n):
        
        if n < 1:
            return 0

        cnt = 0
        sig = 1
        while n/sig:
            temp = sig*10

            cur_digit = (n/sig)%10
            hi_digit = n/temp
            lo_digit = n%sig

            if cur_digit > 1:
                cnt += (hi_digit+1)*sig
            elif cur_digit == 1:
                cnt += hi_digit*sig + (lo_digit+1)
            else:
                cnt += hi_digit*sig

            sig = temp

        return cnt
