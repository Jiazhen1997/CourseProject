



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.cache = {}

    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        
        if N not in self.cache:
            if N == 0:
                ret = []
            elif N == 1:
                ret = [TreeNode(0)]
            else:
                ret = []
                for i in range(N):
                    lefts = self.allPossibleFBT(i)
                    rights = self.allPossibleFBT(N-1-i)
                    
                    if lefts and rights:
                        for left in lefts:
                            for right in rights:
                                node = TreeNode(0)
                                node.left = left
                                node.right = right
                                ret.append(node)
            self.cache[N] = ret

        return self.cache[N]
