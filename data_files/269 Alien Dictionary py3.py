
from typing import List
from collections import defaultdict, deque


class Solution(object):
    def alienOrder(self, words: List[str]) -> str:
        G = self.construct_graph(words)
        visited = defaultdict(int)  
        ret = deque()
        for u in G.keys():
            if visited[u] == 0:
                if not self.topo_dfs(G, u, visited, ret):
                    return ""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 
        Topological sort
        G = defaultdict(list)
        visited = defaultdict(int)  

        pre-condition: u is not visited (0)
        