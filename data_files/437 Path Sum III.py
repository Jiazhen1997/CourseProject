


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict


class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root: TreeNode, target: int) -> int:
        
        self.dfs(root, target, 0, defaultdict(int))
        return self.count

    def dfs(self, node, target, cur_sum, prefix_sum_counter):
        if not node:
            return

        cur_sum += node.val
        
        delta = cur_sum - target
        self.count += prefix_sum_counter[delta]
        if delta == 0:
            self.count += 1

        prefix_sum_counter[cur_sum] += 1
        self.dfs(node.left, target, cur_sum, prefix_sum_counter)
        self.dfs(node.right, target, cur_sum, prefix_sum_counter)
        prefix_sum_counter[cur_sum] -= 1
        

class SolutionComplex:
    def pathSum(self, root, sum):
        
        count = [0]  
        self.dfs(root, sum, 0, {}, count)
        return count[0]

    def dfs(self, root, sum, cur_sum, prefix_sum, count):
        
        if not root:
            return

        cur_sum += root.val
        
        diff = cur_sum - sum
        if diff in prefix_sum:
            count[0] += prefix_sum[diff]
        if diff == 0:  
            count[0] += 1

        prefix_sum[cur_sum] = prefix_sum.get(cur_sum, 0) + 1
        self.dfs(root.left, sum, cur_sum, prefix_sum, count)
        self.dfs(root.right, sum, cur_sum, prefix_sum, count)
        prefix_sum[cur_sum] -= 1  
