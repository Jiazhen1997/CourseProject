
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        
        if not root:
            return []

        result = []
        lst = [root]
        direction = False
        while lst:
            if direction:
                result.append([element.val for element in lst])
            else:
                result.append([element.val for element in reversed(lst)])

            for i in range(len(lst)):  
                element = lst.pop(0)  
                if element.left:
                    lst.append(element.left)
                if element.right:
                    lst.append(element.right)
            direction = not direction
        return result


