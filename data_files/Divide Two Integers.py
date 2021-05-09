
__author__ = 'Daniel'


class Solution:
    def divide(self, dividend, divisor):
        q = 0
        if dividend == 0 or divisor == 0:
            return 0

        
        MAXINT = 2147483647
        MININT = -2147483648
        if dividend == MININT and divisor == -1:
            return MAXINT

        sign = 1 if dividend*divisor > 0 else -1
        dividend, divisor = abs(dividend), abs(divisor)

        d = divisor
        q_cur = 1
        if divisor > dividend:
            return 0

        while d<<1 < dividend:
            d <<= 1
            q_cur <<= 1

        q += q_cur
        dividend -= d

        while dividend:
            if divisor > dividend:
                break

            while d > dividend:
                d >>= 1
                q_cur >>= 1

            q += q_cur
            dividend -= d

        return q*sign

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""d""i""v""i""d""e""(""-""1"","" ""1"")