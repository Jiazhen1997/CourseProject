

USED = True


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False
        if A == B:
            
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            else:
                return False

        
        pair = None
        for i in range(len(A)):
            if A[i] != B[i]:
                if not pair:
                    pair = (A[i], B[i])
                elif pair == (B[i], A[i]):
                    pair = USED
                else:
                    return False

        if pair is None or pair is USED:
            return True

        return False
