

from collections import Counter


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        counts = Counter(str(N))
        for i in range(31):  
            if counts == Counter(str(1 << i)):
                return True
        else:
            return False
