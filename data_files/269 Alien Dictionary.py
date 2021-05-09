

from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def alienOrder(self, words):
        
        V = self.construct_graph(words)
        visited = set()
        pathset = set()
        ret = []
        for v in V.keys():
            if v not in visited:
                if not self.topo_dfs(V, v, visited, pathset, ret):
                    return ""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 
        Topological sort
        :param V: Vertices HashMap
        :param v: currently visiting letter
        :param visited: visited letters
        :param pathset: marked predecessor in the path
        :param ret: the path, ordered  topologically
        :return: whether contains cycles
        
        :param words:
        :param up: upper bound
        :param down: lower bound + 1
        :param ptr: starting index for the char in the word
        :param V: Vertices
        :return: None
        