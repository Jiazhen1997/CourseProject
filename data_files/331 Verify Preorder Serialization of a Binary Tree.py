
__author__ = 'Daniel'


class Solution(object):
    def isValidSerialization(self, preorder):
        
        stk = preorder.split(',')
        child_cnt = 0
        while stk:
            if stk[-1] == '#':
                stk.pop()
                child_cnt += 1
            else:
                child_cnt -= 2
                if child_cnt < 0:
                    return False

                stk.pop()
                child_cnt += 1

        return not stk and child_cnt == 1

    def isValidSerializationSpace(self, preorder):
        
        stk = preorder.split(',')
        child_stk = []
        while stk:
            if stk[-1] == '#':
                child_stk.append(stk.pop())  
            else:
                try:
                    child_stk.pop()
                    child_stk.pop()
                    stk.pop()
                    child_stk.append('#')
                except IndexError:
                    return False

        return not stk and len(child_stk) == 1


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""S""o""l""u""t""i""o""n""("")"".""i""s""V""a""l""i""d""S""e""r""i""a""l""i""z""a""t""i""o""n""(