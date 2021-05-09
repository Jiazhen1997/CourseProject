



class Solution:
    def idx(self, a):
        return a - 1

    def findDuplicates(self, A):
        
        for i in range(len(A)):
            t = self.idx(A[i])
            while i != t:
                if A[i] == A[t]:
                    break
                else:
                    A[i], A[t] = A[t], A[i]
                    t = self.idx(A[i])

        ret = []
        for i in range(len(A)):
            if self.idx(A[i]) != i:
                ret.append(A[i])

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""s""e""t""(""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""D""u""p""l""i""c""a""t""e""s""(""[""4"",""3"",""2"",""7"",""8"",""2"",""3"",""1""]"")"")"" ""=""="" ""s""e""t""(""[""2"",""3""]"")""
