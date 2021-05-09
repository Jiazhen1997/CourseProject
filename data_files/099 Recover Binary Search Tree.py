
__author__ = 'Danyang'

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.val)

class Solution:
    def __init__(self):
        self.swapped_pair = []
        self.current = None
        self.pre = None

    def recoverTree(self, root):
        
        self.in_order(root)
        if len(self.swapped_pair)==2:
            self.swapped_pair[0][0].val, self.swapped_pair[1][1].val = self.swapped_pair[1][1].val, self.swapped_pair[0][0].val
        else: 
            self.swapped_pair[0][0].val, self.swapped_pair[0][1].val = self.swapped_pair[0][1].val, self.swapped_pair[0][0].val
        return root

    def in_order(self, current):
        if not current:
            return

        self.in_order(current.left)
        
        self.pre = self.current
        self.current = current
        if self.pre and not self.pre.val<self.current.val:
            if not self.swapped_pair:
                self.swapped_pair.append((self.pre, self.current))  
            else:
                self.swapped_pair.append((self.pre, self.current))  
        self.in_order(current.right)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""n""o""d""e""1"" ""="" ""T""r""e""e""N""o""d""e""(""2"")""
"" "" "" "" ""n""o""d""e""2"" ""="" ""T""r""e""e""N""o""d""e""(""1"")""
"" "" "" "" ""n""o""d""e""1"".""r""i""g""h""t"" ""="" ""n""o""d""e""2""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""r""e""c""o""v""e""r""T""r""e""e""(""n""o""d""e""1"")