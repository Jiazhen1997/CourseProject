




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import List
from collections import defaultdict


class MerkleHash:
    def __init__(self):
        self.start_key = 0
        self.merkle_hash = defaultdict(self._auto_incr)  

    def _auto_incr(self):
        self.start_key += 1
        return self.start_key

    def __call__(self, val):
        return self.merkle_hash[val]


class Solution:
    def __init__(self):
        self.counter = defaultdict(int)
        self.merkle_hash = MerkleHash()

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        ret = []
        self.walk(root, ret)
        return ret

    def walk(self, cur, ret) -> int:
        
        if not cur:
            return self.merkle_hash(None)

        subtree_value = (cur.val, self.walk(cur.left, ret), self.walk(cur.right, ret))
        merkle_hash = self.merkle_hash(subtree_value)
        if self.counter[merkle_hash] == 1:
            ret.append(cur)

        self.counter[merkle_hash] += 1
        return merkle_hash


class Solution2:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        
        ret = []
        self.walk(root, defaultdict(int), ret)
        return ret

    def walk(self, cur, counter, ret) -> str:
        
        if not cur:
            return "N"o"n"e""
""
"" "" "" "" "" "" "" "" ""c""u""r""_""k""e""y"" ""="" 