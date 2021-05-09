
__author__ = 'Danyang'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.cache = {}

    def generateTrees(self, n):
        
        if n == 0:
            return [None]

        return self.generate_cache(1, n)

    def generate_cache(self, start, end):
        
        if (start, end) not in self.cache:
            roots = []
            if start > end:
                roots.append(None)
                return roots

            for pivot in range(start, end+1):
                left_roots = self.generate_cache(start, pivot-1)
                right_roots = self.generate_cache(pivot+1, end)
                for left_root in left_roots:
                    for right_root in right_roots:
                        root = TreeNode(pivot)
                        root.left = left_root
                        root.right = right_root

                        roots.append(root)

            self.cache[(start, end)] = roots

        return self.cache[(start, end)]

    def generate(self, start, end):
        
        subtree_roots = []

        
        if start > end:
            subtree_roots.append(None)
            return subtree_roots

        
        
        for pivot in range(start, end+1):
            left_subtree_roots = self.generate(start, pivot-1)
            right_subtree_roots = self.generate(pivot+1, end)

            for left_node in left_subtree_roots:
                for right_node in right_subtree_roots:
                    pivot_node = TreeNode(pivot)
                    pivot_node.left = left_node
                    pivot_node.right = right_node

                    subtree_roots.append(pivot_node)

        return subtree_roots
