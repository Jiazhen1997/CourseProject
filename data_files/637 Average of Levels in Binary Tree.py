

from typing import List



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        ret = []
        if not root:
            return ret

        q = [root]
        while q:
            n = len(q)
            avg = sum(map(lambda node: node.val, q)) / n
            ret.append(avg)
            cur_q = []
            for node in q:
                if node.left:
                    cur_q.append(node.left)
                if node.right:
                    cur_q.append(node.right)

            q = cur_q

        return ret
