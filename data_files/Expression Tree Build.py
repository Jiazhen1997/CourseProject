
__author__ = 'Daniel'


class ExpressionTreeNode:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left, self.right = None, None


class Solution:
    def build(self, expression):
        
        post = self.infix2postfix(expression)
        tree_node = self.postfix2tree(post)
        return tree_node

    def infix2postfix(self, expression):
        
        post = []
        op_stk = []
        for elt in expression:
            if elt.isdigit():
                post.append(elt)
            elif elt == "("":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""o""p""_""s""t""k"".""a""p""p""e""n""d""(""e""l""t"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""e""l""t"" ""=""="" 