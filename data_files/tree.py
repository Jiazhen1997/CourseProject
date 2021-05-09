__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Traverser(object):
    def morris_inorder(self, root):
        cur = root
        while cur:
            if not cur.left:
                self.consume(cur)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    self.consume(cur)
                    cur = cur.right

    def morris_preorder(self, root):
        cur = root
        while cur:
            if not cur.left:
                self.consume(cur)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    self.consume(cur)
                    cur = cur.left
                else:
                    pre.right = None
                    cur = cur.right

    def morris_postorder(self, root):
        dummy = TreeNode(0)
        dummy.left = root
        cur = dummy
        while cur:
            if not cur.left:
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    self.consume_path(cur.left, pre)
                    cur = cur.right

    def _reverse(self, fr, to):
        if fr == to: return
        cur = fr
        nxt = cur.right
        while cur and nxt and cur != to:
            nxt.right, cur, nxt = cur, nxt, nxt.right

    def consume_path(self, fr, to):
        self._reverse(fr, to)

        cur = to
        self.consume(cur)
        while cur != fr:
            cur = cur.right
            self.consume(cur)

        self._reverse(to, fr)

    def consume(self, node):
        print node.val


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""r""o""o""t"" ""="" ""T""r""e""e""N""o""d""e""(""6"")""
"" "" "" "" ""r""o""o""t"".""l""e""f""t"" ""="" ""T""r""e""e""N""o""d""e""(""2"")""
"" "" "" "" ""r""o""o""t"".""l""e""f""t"".""l""e""f""t"" ""="" ""T""r""e""e""N""o""d""e""(""1"")""
"" "" "" "" ""r""o""o""t"".""l""e""f""t"".""r""i""g""h""t"" ""="" ""T""r""e""e""N""o""d""e""(""4"")""
"" "" "" "" ""r""o""o""t"".""l""e""f""t"".""r""i""g""h""t"".""l""e""f""t"" ""="" ""T""r""e""e""N""o""d""e""(""3"")""
"" "" "" "" ""r""o""o""t"".""l""e""f""t"".""r""i""g""h""t"".""r""i""g""h""t"" ""="" ""T""r""e""e""N""o""d""e""(""5"")""
"" "" "" "" ""r""o""o""t"".""r""i""g""h""t"" ""="" ""T""r""e""e""N""o""d""e""(""7"")""
"" "" "" "" ""r""o""o""t"".""r""i""g""h""t"".""r""i""g""h""t"" ""="" ""T""r""e""e""N""o""d""e""(""9"")""
"" "" "" "" ""r""o""o""t"".""r""i""g""h""t"".""r""i""g""h""t"".""l""e""f""t"" ""="" ""T""r""e""e""N""o""d""e""(""8"")""
""
"" "" "" "" ""t""r""a""v""e""r""s""e""r"" ""="" ""T""r""a""v""e""r""s""e""r""("")""
"" "" "" "" ""p""r""i""n""t"" ""t""r""a""v""e""r""s""e""r"".""m""o""r""r""i""s""_""i""n""o""r""d""e""r"".""_""_""n""a""m""e""_""_""
"" "" "" "" ""t""r""a""v""e""r""s""e""r"".""m""o""r""r""i""s""_""i""n""o""r""d""e""r""(""r""o""o""t"")""
"" "" "" "" ""p""r""i""n""t"" ""t""r""a""v""e""r""s""e""r"".""m""o""r""r""i""s""_""p""r""e""o""r""d""e""r"".""_""_""n""a""m""e""_""_""
"" "" "" "" ""t""r""a""v""e""r""s""e""r"".""m""o""r""r""i""s""_""p""r""e""o""r""d""e""r""(""r""o""o""t"")""
"" "" "" "" ""p""r""i""n""t"" ""t""r""a""v""e""r""s""e""r"".""m""o""r""r""i""s""_""p""o""s""t""o""r""d""e""r"".""_""_""n""a""m""e""_""_""
"" "" "" "" ""t""r""a""v""e""r""s""e""r"".""m""o""r""r""i""s""_""p""o""s""t""o""r""d""e""r""(""r""o""o""t"")""
""
""
""
""
""
""
