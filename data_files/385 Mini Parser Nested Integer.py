
__author__ = 'Daniel'







class NestedInteger(object):
    def __init__(self, value=None):
        
    def isInteger(self):
        

    def add(self, elem):
        

    def setInteger(self, value):
        

    def getInteger(self):
        

    def getList(self):
        


class Solution(object):
    def deserialize(self, s):
        
        if not s: return None
        stk = []

        i = 0
        while i < len(s):
            if s[i] == '[':
                stk.append(NestedInteger())
                i += 1
            elif s[i] == ']':
                ni = stk.pop()
                if not stk: return ni

                stk[-1].add(ni)
                i += 1
            elif s[i] == ',':
                i += 1
            else:
                j = i
                while j < len(s) and (s[j].isdigit() or s[j] == '-'): j += 1

                ni = NestedInteger(int(s[i: j]) if s[i: j] else None)
                if not stk: return ni
                stk[-1].add(ni)
                i = j

        return stk.pop()


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""d""e""s""e""r""i""a""l""i""z""e""(