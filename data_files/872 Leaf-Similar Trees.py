



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        itr1 = self.dfs(root1)
        itr2 = self.dfs(root2)
        while True:
            a = next(itr1, None)
            b = next(itr2, None)
            if a != b:
                return False
            if a is None and b is None:
                break
        return True

    def dfs(self, node):
        stk = [node]
        
        while stk:
            cur = stk.pop()
            if not cur:
                continue
            if not cur.left and not cur.right:
                yield cur.val
            else:
                stk.append(cur.right)
                stk.append(cur.left)
