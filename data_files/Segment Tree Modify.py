
__author__ = 'Danyang'


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    def modify(self, root, index, value):
        
        if root is None:
            return
        if index < root.start or index > root.end:
            return
        if root.start == index and root.end == index:
            root.max = value
            return

        
        self.modify(root.left, index, value)
        self.modify(root.right, index, value)

        m = value
        if root.left:
            m = max(m, root.left.max)
        if root.right:
            m = max(m, root.right.max)
        root.max = m



