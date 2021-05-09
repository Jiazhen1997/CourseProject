




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def findFrequentTreeSum(self, root):
        
        counter = defaultdict(int)
        self.traverse(root, counter)
        ret = [[], 0]
        for k, v in counter.items():
            if v > ret[1]:
                ret[0] = [k]
                ret[1] = v
            elif v == ret[1]:
                ret[0].append(k)

        return ret[0]

    def traverse(self, root, counter):
        if not root:
            return 0

        cur = root.val
        cur += self.traverse(root.left, counter)
        cur += self.traverse(root.right, counter)
        counter[cur] += 1
        return cur
