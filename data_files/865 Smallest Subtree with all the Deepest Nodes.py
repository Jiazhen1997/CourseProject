




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.deepest = -1
        self.deepest_nodes = None
        self.ret = None

    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        
        self.down(root, 0)
        if len(self.deepest_nodes) == 1:
            return self.deepest_nodes.pop()

        self.count(root)
        return self.ret

    def down(self, node: TreeNode, d: int) -> None:
        if not node:
            return

        if d > self.deepest:
            self.deepest = d
            self.deepest_nodes = set([node])
        elif d == self.deepest:
            self.deepest_nodes.add(node)

        self.down(node.left, d + 1)
        self.down(node.right, d + 1)

    def count(self, node: TreeNode) -> int:
        if not node:
            return 0

        l = self.count(node.left)
        r = self.count(node.right)
        if l != 0 and r != 0 and l + r == len(self.deepest_nodes):
            self.ret = node

        count = l + r
        if node in self.deepest_nodes:
            count += 1
        return count
