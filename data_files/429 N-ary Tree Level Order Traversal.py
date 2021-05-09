




class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        
        if not root:
            return []

        q = [root]
        ret = []
        while q:
            cur = []
            q_new = []
            for e in q:
                q_new.extend(e.children)
                cur.append(e.val)

            ret.append(cur)
            q = q_new

        return ret
