

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        G = graph
        ret = []
        visited = [False for _ in G]
        self.dfs(G, 0, len(G) - 1, [0], visited, ret)
        return ret

    def dfs(self, G, cur, d, cur_path, visited, ret):
        if cur == d:
            ret.append(list(cur_path))
            return 

        for nbr in G[cur]:
            if not visited[nbr]:
                visited[nbr] = True
                cur_path.append(nbr)
                
                self.dfs(G, nbr, d, cur_path, visited, ret)
                cur_path.pop()
                visited[nbr] = False
