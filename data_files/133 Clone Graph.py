
__author__ = 'Danyang'

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
    def __repr__(self):
        return repr(self.label)

class Solution:
    def cloneGraph_TLE(self, node):
        
        return self.clone_graph_visited(node, set())

    def clone_graph_visited(self, node, visited_set):
        
        if not node:
            return
        visited_set.add(node)
        neighbors_cloned = [self.clone_graph_visited(neighbor, set(visited_set)) for neighbor in node.neighbors if neighbor not in visited_set]
        node_cloned = UndirectedGraphNode(node.label)
        for neighbor_cloned in neighbors_cloned:
            if neighbor_cloned not in visited_set:
                neighbor_cloned.neighbors.append(node_cloned)
        node_cloned.neighbors = neighbors_cloned
        return node_cloned

    def cloneGraph(self, node):
        
        if not node:
            return

        original2copy = {} 
        q = [node]  

        clone = UndirectedGraphNode(node.label)
        original2copy[node] = clone
        while q:
            cur = q.pop()
            for neighbor in cur.neighbors:
                if neighbor in original2copy:  
                    original2copy[cur].neighbors.append(original2copy[neighbor])
                else:
                    q.append(neighbor)
                    clone_neighbor = UndirectedGraphNode(neighbor.label)
                    original2copy[neighbor] = clone_neighbor
                    original2copy[cur].neighbors.append(original2copy[neighbor])

        return original2copy[node]


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""l""s""t"" ""="" ""[""U""n""d""i""r""e""c""t""e""d""G""r""a""p""h""N""o""d""e""(""i""+""1"")"" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""3"")""]""
"" "" "" "" ""f""o""r"" ""i""t""e""m"" ""i""n"" ""l""s""t"":""
"" "" "" "" "" "" "" "" ""i""t""e""m"".""n""e""i""g""h""b""o""r""s"" ""="" ""l""i""s""t""(""l""s""t"")""
"" "" "" "" "" "" "" "" ""i""t""e""m"".""n""e""i""g""h""b""o""r""s"".""r""e""m""o""v""e""(""i""t""e""m"")""
"" "" "" "" ""c""l""o""n""e""d"" ""="" ""S""o""l""u""t""i""o""n""("")"".""c""l""o""n""e""G""r""a""p""h""(""l""s""t""[""0""]"")""
"" "" "" "" ""a""s""s""e""r""t"" ""c""l""o""n""e""d"".""n""e""i""g""h""b""o""r""s""[""0""]"".""l""a""b""e""l"" ""i""n"" ""(""2"","" ""3"")""
"" "" "" "" ""a""s""s""e""r""t"" ""c""l""o""n""e""d"".""n""e""i""g""h""b""o""r""s""[""1""]"".""l""a""b""e""l"" ""i""n"" ""(""2"","" ""3"")""
""
""
