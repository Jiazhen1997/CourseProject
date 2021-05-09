




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findMode(self, root):
        
        ret = [[], 0]  
        self.find_mode(root, [None, 0], ret, False)
        self.find_mode(root, [None, 0], ret, True)
        return ret[0]

    def find_mode(self, root, prev, ret, collect):
        
        if not root:
            return

        self.find_mode(root.left, prev, ret, collect)

        if prev[0] == root.val:
            prev[1] += 1
        else:
            prev[1] = 1
        prev[0] = root.val

        if not collect:
            ret[1] = max(ret[1], prev[1])
        else:
            if prev[1] == ret[1]:
                ret[0].append(root.val)

        self.find_mode(root.right, prev, ret, collect)

    def findMode_error(self, root):
        
        if not root:
            return []

        ret = [0, []]
        self.find_mode_error(root, root.val, ret)
        return ret[1]

    def find_mode_error(self, root, target, ret):
        cur = 0
        if not root:
            return cur

        if root.val == target:
            cur += 1
            cur += self.find_mode_error(root.left, root.val, ret)
            cur += self.find_mode_error(root.right, root.val, ret)
            if cur > ret[0]:
                ret[0], ret[1] = cur, [target]
            elif cur == ret[0]:
                ret[1].append(target)
        else:
            self.find_mode_error(root, root.val, ret)

        return cur
