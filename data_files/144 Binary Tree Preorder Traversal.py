
__author__ = 'Danyang'



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        
        ret = []
        cur = root
        while cur:
            if not cur.left:
                ret.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    ret.append(cur.val)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right

        return ret

    def preorderTraversal_memory(self, root):
        
        lst = []
        self.preTraverse_itr(root, lst)
        return lst


    def preTraverse(self, node, lst):
        if not node:
            return
        lst.append(node.val)

        self.preTraverse(node.left, lst)
        self.preTraverse(node.right, lst)

    def preTraverse_itr(self, root, lst):
        
        if not root:
            return
        stk = [root]
        while stk:
            node = stk.pop()
            lst.append(node.val)
            if node.right:  
                stk.append(node.right)

            if node.left:
                stk.append(node.left)



if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""t""1"" ""="" ""T""r""e""e""N""o""d""e""(""1"")""
"" "" "" "" ""t""1"".""l""e""f""t"" ""="" ""T""r""e""e""N""o""d""e""(""2"")""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""p""r""e""o""r""d""e""r""T""r""a""v""e""r""s""a""l""(""t""1"")