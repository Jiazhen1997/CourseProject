
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        
        A = cipher
        N = len(A)
        start = 0
        while start + 1 < N and A[start] <= A[start + 1]:
            start += 1

        
        end = start + 1
        while end + 1 < N and A[end] >= A[end + 1]:
            end += 1

        if end == start + 1:  
            
            j = start + 1
            while j + 1 < N and A[j] < A[j + 1]:
                j += 1

            
            if j != start + 1 and j + 1 == N:  
                return "n"o""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""t""e""s""t"" ""t""a""i""l""i""n""g""
"" "" "" "" "" "" "" "" "" "" "" "" ""i"" ""="" ""j"" ""+"" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""w""h""i""l""e"" ""i"" ""+"" ""1"" ""<"" ""N"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""A""[""i""]"" ""<"" ""A""[""i"" ""+"" ""1""]"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 