
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        
        ret = []
        cur = root
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    ret.append(cur.val)
                    cur = cur.right

        return ret

    def inorderTraversal_memory(self, root):
        
        lst = []
        self.inorderTraverse_itr(root, lst)
        return lst

    def inorderTraverse(self, root, lst):
        
        if not root:
            return
        self.inorderTraverse(root.left, lst)
        lst.append(root.val)
        self.inorderTraverse(root.right, lst)

    def inorderTraverse_itr(self, root, lst):
        
        if not root:
            return

        cur = root
        stk = []
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()  
            lst.append(cur.val)
            cur = cur.right
            
            
            

