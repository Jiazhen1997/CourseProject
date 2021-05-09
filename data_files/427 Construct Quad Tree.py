

__author__ = 'Danyang'



class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid):
        
        l = len(grid)
        return self._construct(grid, 0, 0, l)

    def _construct(self, grid, row, col, l):
        
        if l == 1:
            return Node(grid[row][col], True, None, None, None, None)

        l_child = l // 2
        topLeft = self._construct(grid, row, col, l_child)
        topRight = self._construct(grid, row, col + l_child, l_child)
        bottomLeft = self._construct(grid, row + l_child, col, l_child)
        bottomRight = self._construct(grid, row + l_child, col + l_child, l_child)
        is_leaf = (
            topLeft.val == topRight.val == bottomLeft.val == bottomRight.val
            != "*""
"" "" "" "" "" "" "" "" "")""
"" "" "" "" "" "" "" "" ""i""f"" ""i""s""_""l""e""a""f"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""N""o""d""e""(""g""r""i""d""[""r""o""w""]""[""c""o""l""]"","" ""T""r""u""e"","" ""N""o""n""e"","" ""N""o""n""e"","" ""N""o""n""e"","" ""N""o""n""e"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""N""o""d""e""(