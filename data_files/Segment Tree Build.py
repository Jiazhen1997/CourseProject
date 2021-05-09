
__author__ = 'Danyang'


class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None


class Solution:
    def build(self, start, end):
        
        if start > end:
            return None

        root = SegmentTreeNode(start, end)
        if start == end:
            return root

        root.left = self.build(start, (start+end)/2)
        root.right = self.build((start+end)/2+1, end)
        return root
