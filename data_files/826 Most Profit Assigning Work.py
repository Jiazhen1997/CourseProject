

from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
        tasks = list(sorted(zip(profit, difficulty)))
        worker.sort()
        i = len(tasks) - 1
        j = len(worker) - 1
        ret = 0
        while i >= 0 and j >= 0:
            pro, diff = tasks[i]
            if worker[j] >= diff:
                ret += pro
                j -= 1
            else:
                i -= 1

        return ret
