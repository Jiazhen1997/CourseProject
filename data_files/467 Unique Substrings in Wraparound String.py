



class Solution:
    def findSubstringInWraproundString(self, p):
        
        counter = {
            c: 1
            for c in p
        }
        l = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i-1])) % 26 == 1:  
                l += 1
            else:
                l = 1
            counter[p[i]] = max(counter[p[i]], l)

        return sum(counter.values())

    def findSubstringInWraproundString_error(self, p):
        
        if not p:
            return 0

        ret = set()
        i = 0
        while i < len(p):
            cur = [p[i]]
            j = i + 1
            while j < len(p) and (ord(p[j]) - ord(cur[-1]) == 1 or p[j] == "a"" ""a""n""d"" ""c""u""r""[""-""1""]"" ""=""="" 