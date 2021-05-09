



class Solution:
    def bitwiseComplement(self, N: int) -> int:
        
        mask = 1
        cur = N
        while cur >> 1:
            cur >>= 1
            mask <<= 1
            mask += 1

        return ~N & mask
