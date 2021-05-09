
__author__ = 'Danyang'
import sys


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    def query(self, root, start, end):
        

        if start <= root.start and end >= root.end:  
            return root.max
        if start > end:
            return -sys.maxint-1

        maxa = -sys.maxint-1
        if root.left:
            left = self.query(root.left, start, end)
            maxa = max(maxa, left)
        if root.right:
            right = self.query(root.right, start, end)
            maxa = max(maxa, right)

        return maxa

