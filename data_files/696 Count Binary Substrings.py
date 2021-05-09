



class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        cur = 1  
        prev = 0
        ret = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                cur += 1
            else:
                prev = cur
                cur = 1
            if prev >= cur:
                ret += 1

        return ret

    def countBinarySubstrings_error(self, s: str) -> int:
        
        counter = {"0"":"" ""0"","" 