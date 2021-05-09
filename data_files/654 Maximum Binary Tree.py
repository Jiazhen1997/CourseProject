




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
import heapq


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        stk = []
        for n in nums:
            cur = TreeNode(n)
            while stk and stk[-1].val < cur.val:
                left = stk.pop()
                cur.left = left

            if stk:
                stk[-1].right = cur

            stk.append(cur)

        return stk[0]

class Solution_heap:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        
        if not nums:
            return

        h = [(-v, v) for v in nums]
        idx = {
            v: i
            for i, v in enumerate(nums)
        }
        heapq.heapify(h)
        root = None
        while h:
            _, m = heapq.heappop(h)
            root = self.insert(root, m, idx)

        return root

    def insert(self, node, m, idx):
        if not node:
            return TreeNode(m)

        if idx[m] < idx[node.val]:
            node.left = self.insert(node.left, m, idx)
        elif idx[m] > idx[node.val]:
            node.right = self.insert(node.right, m, idx)
        else:
            raise

        return node
