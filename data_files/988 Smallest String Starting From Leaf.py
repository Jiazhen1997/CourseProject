




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from typing import Tuple
from collections import deque


class Solution:
    def __init__(self):
        self.mn: Tuple[int] = None

    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        self.dfs(root, deque())
        if not self.mn:
            return ""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 