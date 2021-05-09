




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root):
        
        q = [root]
        while q:
            ret = q[0].val
            cur_q = []
            for e in q:
                if e.left:
                    cur_q.append(e.left)
                if e.right:
                    cur_q.append(e.right)
            q = cur_q

        return ret
