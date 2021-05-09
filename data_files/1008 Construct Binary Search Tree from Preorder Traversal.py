

from typing import List



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder2(self, preorder: List[int]) -> TreeNode:
        
        root = TreeNode(preorder[0])
        stk = [root]
        for a in preorder[1:]:
            node = TreeNode(a)
            if a < stk[-1].val:  
                stk[-1].left = node
            else:
                while len(stk) >= 2 and stk[-2].val < a:
                    stk.pop()

                stk[-1].right = node
                stk.pop()

            stk.append(node)

        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        root = TreeNode(preorder[0])
        stk = [root]
        for a in preorder[1:]:
            node = TreeNode(a)
            if a < stk[-1].val:
                stk[-1].left = node
            else:
                while stk and stk[-1].val < a:
                    pi = stk.pop()
                pi.right = node
            stk.append(node)
            
        return root
