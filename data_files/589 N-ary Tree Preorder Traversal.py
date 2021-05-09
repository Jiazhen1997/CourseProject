




class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


from typing import List


class Solution:
    def preorder(self, root: "N"o"d"e"")"" ""-"">"" ""L""i""s""t""[""i""n""t""]"":""
"" "" "" "" "" "" "" "" 
        ret = []
        if not root:
            return ret

        stk = [root]
        while stk:
            cur = stk.pop()
            ret.append(cur.val)
            for c in reversed(cur.children):
                stk.append(c)

        return ret
