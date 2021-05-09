


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        
        ret = set()
        cur = set()  
        for a in A:
            cur = {a | e for e in cur} | {a}
            ret |= cur

        return len(ret)
