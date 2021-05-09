



class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        targets = set(J)
        ret = 0
        for c in S:
            if c in targets:
                ret += 1

        return ret
