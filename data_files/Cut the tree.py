

__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, item):
        self.item = item
        self.tree_sum = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.item)


class Solution_error(object):
    def solve(self, cipher):
        
        root = self.construct_tree(cipher)
        total = self.get_tree_sum(root)
        mini = [1 << 32]  
        self.dfs(root, total, mini)
        return mini[0]

    def dfs(self, root, total, mini):
        
        if not root:
            return

        mini[0] = min(mini[0], abs(total - root.tree_sum - root.tree_sum))
        self.dfs(root.left, total, mini)
        self.dfs(root.right, total, mini)


    def construct_tree(self, cipher):
        
        N, nodes, rls = cipher
        lst = [TreeNode(val) for val in nodes]
        
        
        rls = map(lambda x: [x[0] - 1, x[1] - 1], rls)
        linked_set = {0}
        for r in rls:
            if r[0] in linked_set:
                parent = r[0]
                child = r[1]
            else:
                parent = r[1]
                child = r[0]

            linked_set.add(child)
            if not lst[parent].left:
                lst[parent].left = lst[child]
            else:
                lst[parent].right = lst[child]

        return lst[0]

    def get_tree_sum(self, root):
        
        if not root.tree_sum:
            left_sum = self.get_tree_sum(root.left) if root.left else 0
            right_sum = self.get_tree_sum(root.right) if root.right else 0
            root.tree_sum = left_sum + right_sum + root.item

        return root.tree_sum








class Solution(object):
    def __init__(self):
        self.order = 0

    def __inc_order(self):
        self.order += 1
        return self.order

    def solve(self, cipher):
        
        N, data, rls = cipher

        
        visited = [-1 for _ in xrange(N)]  
        E = [(0, 0) for _ in xrange(N - 1)]
        G = [[] for _ in xrange(N)]
        v_sum = [-1 for _ in xrange(N)]  
        _sum = sum(data)

        
        for ind, r in enumerate(rls):
            u = r[0] - 1
            v = r[1] - 1

            G[u].append(v)
            G[v].append(u)

            E[ind] = (u, v)

        
        
        
        
        
        
        
        
        

        
        
        def get_sum(s):
            if v_sum[s] == -1:
                visited[s] = self.__inc_order()
                v_sum[s] = data[s]
                for n in G[s]:  
                    if visited[n] == -1:
                        v_sum[s] += get_sum(n)
            return v_sum[s]

        get_sum(0)

        mini = 1 << 32
        for e in E:
            u, v = e
            if visited[u] > visited[v]:  
                mini = min(mini, abs(_sum - get_sum(u) - get_sum(u)))
            else:
                mini = min(mini, abs(_sum - get_sum(v) - get_sum(v)))
        return mini


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""s""y""s"".""s""e""t""r""e""c""u""r""s""i""o""n""l""i""m""i""t""(""1""0""0""0""0""0"")"" "" ""#"" ""o""t""h""e""r""w""i""s""e"" ""n""o""t"" ""e""n""o""u""g""h"","" ""s""t""a""c""k"" ""p""r""o""b""l""e""m"" ""w""i""t""h"" ""p""y""t""h""o""n""
"" "" "" "" ""#"" ""p""r""i""n""t"" ""s""y""s"".""g""e""t""r""e""c""u""r""s""i""o""n""l""i""m""i""t""("")""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(