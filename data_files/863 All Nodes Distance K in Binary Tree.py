




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        ret = []
        self.ancestor_dist(root, K, target, ret)
        return ret

    def dfs_down(self, node, d, ret):
        
        if not node:
            return
        if d == 0:
            ret.append(node.val)
        else:
            self.dfs_down(node.left, d - 1, ret)
            self.dfs_down(node.right, d - 1, ret)

    def ancestor_dist(self, node, K, target, ret):
        if not node:
            return float('inf')

        if node.val == target.val:
            
            self.dfs_down(node, K, ret)
            return 0
        else:
            l = self.ancestor_dist(node.left, K, target, ret)
            r = self.ancestor_dist(node.right, K, target, ret)
            d = min(l, r) + 1
            if d == K:
                ret.append(node.val)
            elif l == float('inf'):
                self.dfs_down(node.left, K - d - 1, ret)
            else:  
                self.dfs_down(node.right, K - d - 1, ret)
            return d


class SolutionComplicated:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        ret = []
        self.dfs1(target, K, ret)
        hm = {}
        self.ancestor_dist(root, target, hm)
        self.dfs2(root, target, K, float("i"n"f"")"","" ""h""m"","" ""r""e""t"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
""
"" "" "" "" ""d""e""f"" ""d""f""s""1""(""s""e""l""f"","" ""n""o""d""e"","" ""K"","" ""r""e""t"")"":""
"" "" "" "" "" "" "" "" 
        if not node:
            return

        if K == 0:
            ret.append(node.val)
        else:
            self.dfs1(node.left, K-1, ret)
            self.dfs1(node.right, K-1, ret)

    def ancestor_dist(self, node, target, hm):
        if not node:
            return float('inf')

        if node.val == target.val:
            hm[node.val] = 0
        else:
            left = self.ancestor_dist(node.left, target, hm)
            right = self.ancestor_dist(node.right, target, hm)
            hm[node.val] = min(left, right) + 1

        return hm[node.val]

    def dfs2(self, node, target, K, dist, hm, ret):
        
        if not node:
            return

        if node.val == target.val:
            return

        dist = min(dist, hm[node.val])
        if dist == K:
            ret.append(node.val)

        self.dfs2(node.left, target, K, dist + 1, hm, ret)
        self.dfs2(node.right, target, K, dist + 1, hm, ret)
