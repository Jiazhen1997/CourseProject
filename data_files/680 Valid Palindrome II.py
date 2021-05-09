



class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                
                
                return self.is_palindrome(s[i:j]) or self.is_palindrome(s[i+1:j+1])

        return True

    def is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""v""a""l""i""d""P""a""l""i""n""d""r""o""m""e""(