



class TreeNode:
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None


class Solution:
    def deleteNode(self, root, key):
        
        return self._delete(root, key)

    def _delete(self, root, key):
        
        if not root:
            return

        
        if key < root.val:
            root.left = self._delete(root.left, key)
            return root
        elif key > root.val:
            root.right = self._delete(root.right, key)
            return root
        else:
            if root.left:
                maxa, left = self._pop_max(root.left)
                root.left = left
                root.val = maxa
                return root
            elif root.right:
                mini, right = self._pop_min(root.right)
                root.right = right
                root.val = mini
                return root
            else:
                return

    def _pop_max(self, root):
        if root.right:
            maxa, right = self._pop_max(root.right)
            root.right = right
            return maxa, root
        
        else:
            return root.val, root.left

    def _pop_min(self, root):
        if root.left:
            mini, left = self._pop_min(root.left)
            root.left = left
            return mini, root
        
        else:
            return root.val, root.right

    def _delete_error(self, root, key):
        
        if not root:
            return

        
        if key < root.val:
            root.left = self._delete(root.left, key)
            return root
        elif key > root.val:
            root.right = self._delete(root.right, key)
            return root
        else:
            if root.left:
                root.val = root.left.val
                left = self._delete(root.left, root.left.val)
                root.left = left
                return root
            elif root.right:
                root.val = root.right.val
                right = self._delete(root.right, root.right.val)
                root.right = right
                return root
            else:
                return
