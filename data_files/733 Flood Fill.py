

from typing import List
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        cur_color = image[sr][sc]
        if cur_color == newColor:
            return image

        self.dfs(image, sr, sc, cur_color, newColor)
        return image

    def dfs(self, image, i, j, cur_color, new_color):
        image[i][j] = new_color
        m, n = len(image), len(image[0])
        for di, dj in dirs:
            I = i + di
            J = j + dj
            if 0 <= I < m and 0 <= J < n and image[I][J] == cur_color:
                self.dfs(image, I, J, cur_color, new_color)
