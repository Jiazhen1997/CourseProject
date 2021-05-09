




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ret = 0

    def distributeCoins(self, root: TreeNode) -> int:
        
        self.demand(root)
        return self.ret

    def demand(self, node) -> int:
        if not node:
            return 0

        demand_l = self.demand(node.left)
        demand_r = self.demand(node.right)
        demand_m = 1 - node.val
        
        demand = demand_l + demand_r + demand_m
        self.ret += abs(demand)
        return demand
