



class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        A = [(a - b, a, b) for a, b in costs]
        A.sort()
        ret = 0
        remain = len(A) // 2
        for _, a, b in A:
            if remain > 0:
                ret += a
                remain -= 1
            else:
                ret += b

        return ret

    def twoCitySchedCost_error(self, costs: List[List[int]]) -> int:
        
        A = [(abs(a - b), a, b) for a, b in costs]
        A.sort(reverse=True)
        ret = 0
        remain = len(A) // 2
        for _, a, b in A:
            if a > b:
                ret += b
            elif remain > 0:
                ret += a
                remain -= 1
            else:
                ret += b

        return ret
