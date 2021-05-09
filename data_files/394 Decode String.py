
__author__ = 'Daniel'


class Solution(object):
    def decodeString(self, s):
        
        stk = [
            [1, []]
        ]  
        i = 0
        while i < len(s):
            if s[i].isdigit():  
                j = i+1
                while s[j] != '[': j += 1
                stk.append([
                    int(s[i:j]), []
                ])
                i = j+1
            elif s[i].islower():  
                stk[-1][1].append(s[i])
                i += 1
            elif s[i] == ']':  
                cnt, partial = stk.pop()
                partial = ''.join(partial) * cnt
                stk[-1][1].append(partial)
                i += 1

        return ''.join(stk.pop()[1])


class SolutionVerbose(object):
    def decodeString(self, s):
        
        stk = []
        i = 0
        ret = []
        while i < len(s):
            if s[i].isdigit():  
                j = i+1
                while s[j] != '[': j += 1
                stk.append([
                    int(s[i:j]), []
                ])
                i = j+1
            elif s[i].islower():  
                if not stk:
                    ret.append(s[i])
                else:
                    stk[-1][1].append(s[i])
                i += 1
            elif s[i] == ']':  
                cnt, partial = stk.pop()
                partial = ''.join(partial) * cnt
                if not stk:
                   ret.append(partial)
                else:
                    stk[-1][1].append(partial)

                i += 1

        return ''.join(ret)


class SolutionError(object):
    def decodeString(self, s):
        
        stk = []
        i = 0
        ret = []
        while i < len(s):
            if s[i].isdigit():
                j = i + 1
                while s[j] != '[': j += 1
                prev = stk[-1] if stk else 1
                stk.append(prev * int(s[i:j]))
                i = j + 1
            elif s[i].islower():
                repeat = stk[-1] if stk else 1
                for _ in xrange(repeat): ret.append(s[i])
                i += 1
            elif s[i] == ']':
                stk.pop()
                i += 1

        return ''.join(ret)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""d""e""c""o""d""e""S""t""r""i""n""g""(""'""2""[""a""b""c""]""3""[""c""d""]""e""f""'"")"" ""=""="" ""'""a""b""c""a""b""c""c""d""c""d""c""d""e""f""'""
""
""
""
""
