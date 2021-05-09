



class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        m, n = len(name), len(typed)
        i, j = 0, 0
        while i < m and j < n:
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif j - 1 >= 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False

        
        while j - 1 >= 0 and j < n and typed[j-1] == typed[j]:
            j += 1

        return i == m and j == n
