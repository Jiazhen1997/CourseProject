



class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        
        l = 0
        for s in S:
            if s.isdigit():
                l *= int(s)
            else:
                l += 1

        
        for s in reversed(S):
            K %= l
            if K == 0 and s.isalpha():
                
                return s
            if s.isdigit():
                l //= int(s)
            else:
                l -= 1

        raise

    def decodeAtIndex_error(self, S: str, K: int) -> str:
        
        K -= 1  
        i = 0
        j = 0
        last = None
        n = len(S)
        while j < n:
            if S[j].isdigit():
                if not last:
                    last = j

                d = int(S[j])
                l = last - i
                while K >= l and d > 0:
                    K -= l
                    d -= 1
                if d > 0:
                    return S[i + K]
            elif last:
                    i = j
                    last = None

            j += 1

        return S[i+K]


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""d""e""c""o""d""e""A""t""I""n""d""e""x""(