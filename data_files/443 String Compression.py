



class Solution:
    def compress(self, chars):
        
        ret = 1
        s = 0  
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[s]:
                continue
            l = i - s
            if l > 1:
                for digit in str(l):
                    chars[ret] = digit
                    ret += 1
            if i < len(chars):
                chars[ret] = chars[i]
                ret += 1
                s = i
                
        return ret

    def compress_error(self, chars):
        
        s = 0
        for idx in range(1, len(chars) + 1):
            if idx < len(chars) and chars[idx] == chars[s]:
                continue
            l = idx - s
            if l == 1:
                s = min(s + 1, len(chars) - 1)
            else:
                for digit in str(l):
                    s += 1
                    chars[s] = digit
                if idx < len(chars):
                    s += 1
                    chars[s] = chars[idx]
        return s + 1


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""m""p""r""e""s""s""(""[