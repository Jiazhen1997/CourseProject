




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        
        if not root:
            return 0

        ret = 0
        q = [(0, root)]  
        while q:
            cur_q = []
            left, right = q[0][0], q[-1][0]
            ret = max(ret, right - left + 1)
            for idx, node in q:
                if node.left:
                    cur_q.append((idx * 2, node.left))
                if node.right:
                    cur_q.append((idx * 2 + 1, node.right))

            q = cur_q

        return ret
