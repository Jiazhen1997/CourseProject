
__author__ = 'Daniel'
DEFAULT = 0
f = lambda x, y: x+y


class Solution:
    def query(self, root, s, e):
        
        if not root:
            return DEFAULT

        if s <= root.start and e >= root.end:
            return root.count

        if s > root.end or e < root.start:
            return DEFAULT

        l = self.query(root.left, s, e)
        r = self.query(root.right, s, e)
        return f(l, r)
