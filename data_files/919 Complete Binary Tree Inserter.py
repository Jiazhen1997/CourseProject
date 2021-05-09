




class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class CBTInserter:
    def __init__(self, root: TreeNode):
        
        self.candidates = deque()
        self.root = root
        q = [root]  
        while q:
            cur_q = []
            for e in q:
                if e.left:
                    cur_q.append(e.left)
                if e.right:
                    cur_q.append(e.right)
                if not e.left or not e.right:
                    
                    self.candidates.append(e)
            q = cur_q

    def insert(self, v: int) -> int:
        pi = self.candidates[0]
        node = TreeNode(v)
        if not pi.left:
            pi.left = node
        else:
            pi.right = node

        if pi.left and pi.right:
            self.candidates.popleft()

        self.candidates.append(node)
        return pi.val

    def get_root(self) -> TreeNode:
        return self.root






