



class Solution:
    def reachNumber(self, target: int) -> int:
        
        target = abs(target)
        s = 0
        k = 0
        while s < target:
            k += 1
            s += k

        delta = s - target
        if delta % 2 == 0:
            return k
        else:  
            if (k + 1) % 2 == 1:
                return k + 1
            else:
                return k + 2
