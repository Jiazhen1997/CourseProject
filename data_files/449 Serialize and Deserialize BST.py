



class TreeNode(object):
  def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None


class Codec:
    DELIMITER = ",""
""
"" "" "" "" ""d""e""f"" ""s""e""r""i""a""l""i""z""e""(""s""e""l""f"","" ""r""o""o""t"")"":""
"" "" "" "" "" "" "" "" 
        def traverse(root, ret):
            if not root:
                return

            ret.append(root.val)
            traverse(root.left, ret)
            traverse(root.right, ret)

        ret = []
        traverse(root, ret)
        return self.DELIMITER.join(map(str, ret))

    def deserialize(self, data):
        
        if not data:
            return
            
        lst = list(map(int, data.split(self.DELIMITER)))
        root = TreeNode(lst[0])
        def insert(root, val):
            
            if val < root.val:
                if not root.left:
                    root.left = TreeNode(val)
                else:
                    insert(root.left, val)
            else:
                if not root.right:
                    root.right = TreeNode(val)
                else:
                    insert(root.right, val)

        for a in lst[1:]:
            insert(root, a)

        return root





