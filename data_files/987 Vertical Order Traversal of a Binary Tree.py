




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def __init__(self):
        self.mp = defaultdict(list)  

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.dfs(root, 0, 0)
        ret = []
        mn = min(self.mp)
        mx = max(self.mp)
        for i in range(mn, mx+1):
            ret.append([
                val
                for _, val in sorted(self.mp[i])
            ])
        return ret

    def dfs(self, node, x, y):
        if not node:
            return
        self.mp[x].append((-y, node.val))
        self.dfs(node.left, x-1, y-1)
        self.dfs(node.right, x+1, y-1)
