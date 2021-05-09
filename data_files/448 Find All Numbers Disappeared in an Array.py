



class Solution:
    def findDisappearedNumbers(self, A):
        
        for idx in range(len(A)):
            while True:
                target = A[idx] - 1
                if idx == target or A[idx] == A[target]:
                    break 
                A[idx], A[target] = A[target], A[idx]

        missing = []
        for idx, elm in enumerate(A):
            if idx != elm - 1:
                missing.append(idx + 1)
        return missing


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""D""i""s""a""p""p""e""a""r""e""d""N""u""m""b""e""r""s""(""[""4"","" ""3"","" ""2"","" ""7"","" ""8"","" ""2"","" ""3"","" ""1""]"")"" ""=""="" ""[""5"","" ""6""]""
