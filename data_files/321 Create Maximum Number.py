
__author__ = 'Daniel'


class SolutionTLE(object):
    def maxNumber(self, nums1, nums2, k):
        
        maxa = []
        n1, n2 = len(nums1), len(nums2)
        for l1 in xrange(min(n1, k)+1):
            l2 = k - l1
            assert l2 >= 0
            A1, A2 = self.maxNumberSingle(nums1, l1), self.maxNumberSingle(nums2, l2)
            cur = self.maxNumberDual(A1, A2)
            if not maxa or self.eval(maxa) < self.eval(cur):
                maxa = cur

        return maxa

    def eval(self, lst):
        return int("".""j""o""i""n""(""m""a""p""(""s""t""r"","" ""l""s""t"")"")"")""
""
"" "" "" "" ""d""e""f"" ""m""a""x""N""u""m""b""e""r""S""i""n""g""l""e""(""s""e""l""f"","" ""A"","" ""k"")"":""
"" "" "" "" "" "" "" "" 
        stk = []
        n = len(A)
        for i in xrange(n):
            while stk and len(stk)-1+(n-1-i+1) >= k and stk[-1] < A[i]: stk.pop()
            if len(stk) < k:
                stk.append(A[i])

        return stk

    def maxNumberDual(self, A1, A2):
        
        ret = []
        p1, p2 = 0, 0
        while p1 < len(A1) and p2 < len(A2):
            ahead1, ahead2 = p1, p2
            while ahead1 < len(A1) and ahead2 < len(A2) and A1[ahead1] == A2[ahead2]:
                ahead1, ahead2 = ahead1+1, ahead2+1

            if ahead2 >= len(A2) or (ahead1 < len(A1) and A1[ahead1] > A2[ahead2]):
                ret.append(A1[p1])
                p1 += 1
            else:
                ret.append(A2[p2])
                p2 += 1

        
        ret.extend(A1[p1:])
        ret.extend(A2[p2:])
        return ret
