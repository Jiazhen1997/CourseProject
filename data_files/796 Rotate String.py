



class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        
        if len(A) != len(B):
            return False

        if not A and not B:
            return True

        for i in range(1, len(A)):
            for j in range(len(B)):
                if A[(i + j) % len(A)] != B[j]:
                    break
            else:
                return True

        return False
