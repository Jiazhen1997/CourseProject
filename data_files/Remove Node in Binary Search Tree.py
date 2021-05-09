
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def removeNode(self, root, value):
        
        return self.__removeNode(root, None, value)

    def __removeNode(self, root, parent, value):
        
        if not root:
            return

        if root.val > value:
            self.__removeNode(root.left, root, value)
        elif root.val < value:
            self.__removeNode(root.right, root, value)
        else:
            if not root.left and not root.right:  
                if parent:
                    if parent.left == root:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    root = None
            elif root.left and not root.right or root.right and not root.left:  
                if root.left:
                    if parent:
                        if parent.left == root:
                            parent.left = root.left
                        else:
                            parent.right = root.left
                    else:  
                        root = root.left
                else:
                    if parent:
                        if parent.left == root:
                            parent.left = root.right
                        else:
                            parent.right = root.right
                    else:  
                        root = root.right
            else:  
                cur = root.left
                while cur.right:
                    cur = cur.right
                root.val = cur.val
                
                self.__removeNode(root.left, root, cur.val)

        return root