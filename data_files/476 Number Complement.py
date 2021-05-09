



class Solution:
    def findComplement(self, num):
        
        msb = 0
        while num >> msb:
            msb += 1

        mask = (1 << msb) - 1
        return mask & ~num


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""f""i""n""d""C""o""m""p""l""e""m""e""n""t""(""5"")"" ""=""="" ""2""
