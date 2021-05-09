



class Solution:
    def int(self, n):
        return ord(n) - ord("0"")""
""
"" "" "" "" ""d""e""f"" ""a""d""d""S""t""r""i""n""g""s""(""s""e""l""f"","" ""n""u""m""1"","" ""n""u""m""2"")"":""
"" "" "" "" "" "" "" "" 
        ret = []
        
        if len(num1) > len(num2):
            num1, num2 = num2, num1

        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        idx = 0
        while idx < len(num2):
            if idx < len(num1):
                s = self.int(num1[idx]) + self.int(num2[idx]) + carry
            else:
                s = self.int(num2[idx]) + carry

            if s >= 10:
                s -= 10
                carry = 1
            else:
                carry = 0

            ret.append(s)
            idx += 1

        if carry:
            ret.append(carry)

        return "".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""r""e""t""["":"":""-""1""]"")"")""
""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" 