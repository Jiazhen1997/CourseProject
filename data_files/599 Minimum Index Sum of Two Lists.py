

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {}
        for i, v in enumerate(list2):
            index[v] = i

        ret = []
        mini = float('inf')
        for i, v in enumerate(list1):
            if v in index:
                cur = i + index[v]  
                if cur < mini:
                    mini = cur
                    ret = [v]
                elif cur == mini:
                    ret.append(v)

        return ret
