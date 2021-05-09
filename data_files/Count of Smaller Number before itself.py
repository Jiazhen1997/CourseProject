
__author__ = 'Daniel'


class Node(object):
    def __init__(self, val):
        
        self.val = val
        self.cnt_left = 0
        self.cnt_this = 0
        self.left, self.right = None, None

    def __repr__(self):
        return repr(self.val)


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        
        if not root:
            root = Node(val)

        if root.val == val:
            root.cnt_this += 1
        elif val < root.val:
            root.cnt_left += 1
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def rank(self, root, val):
        
        if not root:
            return 0
        if root.val < val:
            return root.cnt_this+root.cnt_left+self.rank(root.right, val)
        elif root.val == val:
            return root.cnt_left
        else:
            return self.rank(root.left, val)


class Solution(object):
    def countOfSmallerNumberII(self, A):
        
        tree = BST()
        ret = []
        for a in A:
            tree.root = tree.insert(tree.root, a)
            ret.append(tree.rank(tree.root, a))

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""u""n""t""O""f""S""m""a""l""l""e""r""N""u""m""b""e""r""I""I""(""
"" "" "" "" "" "" "" "" ""[""2""6"","" ""7""8"","" ""2""7"","" ""1""0""0"","" ""3""3"","" ""6""7"","" ""9""0"","" ""2""3"","" ""6""6"","" ""5"","" ""3""8"","" ""7"","" ""3""5"","" ""2""3"","" ""5""2"","" ""2""2"","" ""8""3"","" ""5""1"","" ""9""8"","" ""6""9"","" ""8""1"","" ""3""2"","" ""7""8"","" ""2""8"","" ""9""4"","" ""1""3"","" ""2"","" ""9""7"",""
"" "" "" "" "" "" "" "" "" ""3"","" ""7""6"","" ""9""9"","" ""5""1"","" ""9"","" ""2""1"","" ""8""4"","" ""6""6"","" ""6""5"","" ""3""6"","" ""1""0""0"","" ""4""1""]"")"" ""=""="" ""[""0"","" ""1"","" ""1"","" ""3"","" ""2"","" ""3"","" ""5"","" ""0"","" ""4"","" ""0"","" ""5"","" ""1"","" ""6"","" ""2"","" ""9"","" ""2"","" ""1""4"","" ""1""0"","" ""1""7"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""1""4"","" ""1""6"","" ""7"","" ""1""6"","" ""7"","" ""2""2"","" ""2"","" ""0"","" ""2""5"","" ""1"","" ""2""0"","" ""2""9"","" ""1""5"","" ""4"","" ""6"","" ""2""8"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""2""0"","" ""2""0"","" ""1""6"","" ""3""7"","" ""1""8""]""
