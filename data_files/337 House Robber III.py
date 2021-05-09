
__author__ = 'Daniel'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.cache_rob = {}
        self.cache_notrob = {}

    def rob(self, root):
        
        if root is None:
            return 0

        if root not in self.cache_rob:
            val = max(
                self.notrob(root),
                root.val + self.notrob(root.left) + self.notrob(root.right)
            )
            self.cache_rob[root] = val

        return self.cache_rob[root]

    def notrob(self, root):
        
        if root is None:
            return 0

        if root not in self.cache_notrob:
            val = (
                self.rob(root.left) +
                self.rob(root.right)
            )

            self.cache_notrob[root] = val

        return self.cache_notrob[root]


class SolutionTLE(object):
    def rob(self, root):
        
        if root is None:
            return 0

        return max(
            self.dorob(root),
            self.notrob(root)
        )

    def dorob(self, root):
        if root is None:
            return 0

        return (
            root.val +
            self.notrob(root.left) +
            self.notrob(root.right)
        )

    def notrob(self, root):
        if root is None:
            return 0

        return (max(self.notrob(root.left), self.rob(root.left)) +
                    max(self.notrob(root.right), self.rob(root.right)))
