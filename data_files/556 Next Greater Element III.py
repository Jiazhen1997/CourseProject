



class Solution:
    def nextGreaterElement(self, n: int) -> int:
        
        seq = list(str(n))
        N = len(seq)
        if N < 2:
            return -1

        
        i = N - 2
        while seq[i] >= seq[i+1]:
            i -= 1
            if i < 0:
                return -1

        j = N - 1
        while seq[i] >= seq[j]:
            j -= 1

        seq[i], seq[j] = seq[j], seq[i]
        seq[i+1:] = reversed(seq[i+1:])
        ret = int("".""j""o""i""n""(""s""e""q"")"")""
"" "" "" "" "" "" "" "" ""i""f"" ""r""e""t"" ""<""="" ""1"" ""<""<"" ""3""1"" ""-"" ""1"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""-""1""
""
"" "" "" "" ""d""e""f"" ""n""e""x""t""G""r""e""a""t""e""r""E""l""e""m""e""n""t""_""s""o""r""t""(""s""e""l""f"","" ""n"":"" ""i""n""t"")"" ""-"">"" ""i""n""t"":""
"" "" "" "" "" "" "" "" 
        seq = [int(e) for e in str(n)]
        stk = []  
        for i in range(len(seq) - 1, -1 , -1):
            e = seq[i]
            popped = None
            while stk and seq[stk[-1]] > e:
                popped = stk.pop()

            if popped:
                seq[i], seq[popped] = seq[popped], seq[i]
                seq[i+1:] = sorted(seq[i+1:])  
                ret = int("".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""s""e""q"")"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""r""e""t"" ""<""="" ""1"" ""<""<"" ""3""1"" ""-"" ""1"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""t""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""-""1""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""t""k"".""a""p""p""e""n""d""(""i"")""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""-""1""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 