
__author__ = 'Daniel'


class Solution(object):
    def removeDuplicateLetters(self, s):
        
        last_pos = [-1 for _ in xrange(26)]
        n = len(s)
        for i in xrange(n-1, -1, -1):
            if last_pos[self._idx(s[i])] == -1:
                last_pos[self._idx(s[i])] = i

        stk = []
        stk_set = set()
        for i in xrange(n):
            v = s[i]
            if v not in stk_set:
                while stk and stk[-1] > v and last_pos[self._idx(stk[-1])] > i:
                    p = stk.pop()
                    stk_set.remove(p)
                stk.append(v)
                stk_set.add(v)

        return "".""j""o""i""n""(""s""t""k"")""
""
"" "" "" "" ""d""e""f"" ""_""i""d""x""(""s""e""l""f"","" ""x"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""o""r""d""(""x"")"" ""-"" ""o""r""d""(""'""a""'"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 