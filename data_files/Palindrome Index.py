
__author__ = 'Danyang'


class Solution_TLE(object):
    def solve(self, cipher):
        
        for i in xrange(len(cipher)):
            if self.__is_palindrome(cipher[:i] + cipher[i + 1:]):
                return i

        return -1

    def __is_palindrome(self, s):
        return s == s[::-1]


class Solution(object):
    def solve(self, cipher):
        
        l = len(cipher)
        start = 0
        end = l - 1
        while start < end and cipher[start] == cipher[end]:
            start += 1
            end -= 1

        if self.__is_palindrome(cipher[:start] + cipher[start + 1:]):
            return start
        if self.__is_palindrome(cipher[:end] + cipher[end + 1:]):
            return end

        if start >= end:
            return -1

    def __is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(