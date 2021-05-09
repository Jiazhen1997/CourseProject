

from collections import defaultdict


class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        
        G = defaultdict(lambda: defaultdict(int))
        G[0][0] = poured
        for i in range(query_row):
            for j in range(i+1):  
                excess = max(0, G[i][j] - 1)
                G[i+1][j] += excess / 2
                G[i+1][j+1] += excess / 2

        return min(1, G[query_row][query_glass])
