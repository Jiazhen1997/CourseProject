

from typing import List



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        stk = []
        popped = None
        j = 0
        for e in pre:
            stk.append(TreeNode(e))
            while stk and stk[-1].val == post[j]:
                popped = stk.pop()
                j += 1
                if stk:
                    if not stk[-1].left:
                        stk[-1].left = popped
                    else:
                        stk[-1].right = popped

        assert j == len(post)
        return popped  

    def constructFromPrePost_complex(self, pre: List[int], post: List[int]) -> TreeNode:
        
        if not pre or not post:
            return None

        root = TreeNode(pre[0])
        if len(pre) == 1:
            return root

        if pre[1] == post[-2]:
            
            left = None
            right = self.constructFromPrePost(pre[1:], post[:-1])
        else:
            l = 0
            for a in post:
                l += 1
                if a == pre[1]:
                    break
            else:
                raise

            left = self.constructFromPrePost(pre[1:1+l], post[:l])
            right = self.constructFromPrePost(pre[1+l:], post[l:-1])

        root.left = left
        root.right = right
        return root
