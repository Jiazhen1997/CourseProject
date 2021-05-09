




class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


from typing import List
from collections import deque


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
        if not root:
            return []

        ret = deque()
        stk = [root]
        visited = set()
        while stk:
            cur = stk.pop()
            ret.appendleft(cur.val)
            for c in cur.children:
                stk.append(c)

        return list(ret)
        
    def postorder_visited(self, root: 'Node') -> List[int]:
        
        ret = []
        if not root:
            return ret

        stk = [root]
        visited = set()
        while stk:
            cur = stk[-1]
            if cur in visited:
                stk.pop()
                ret.append(cur.val)
            else:
                visited.add(cur)
                for c in reversed(cur.children):
                    stk.append(c)

        return ret
