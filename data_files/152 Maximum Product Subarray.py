
__author__ = 'Danyang'


class Solution(object):
    def maxProduct_oneline(self, nums):
        return max(reduce(lambda A, n: [max(A), min(n, A[1]*n, A[2]*n), max(n, A[1]*n, A[2]*n)], nums[1:], [nums[0]]*3))

    def maxProduct(self, nums):
        
        small = nums[0]
        large = nums[0]
        maxa = nums[0]
        for a in nums[1:]:
            small, large = min(a, small*a, large*a), max(a, small*a, large*a)
            maxa = max(maxa, small, large)

        return maxa

    def maxProduct_error2(self, nums):
        
        if len(nums) < 2:
            return max(nums)

        n = len(nums)
        F_pos = [0 for _ in xrange(n+1)]
        F_neg = [0 for _ in xrange(n+1)]

        maxa = 1
        for i in xrange(1, n+1):
            v = nums[i-1]
            if v > 0:
                F_pos[i] = F_pos[i-1]*v if F_pos[i-1] != 0 else v
                F_neg[i] = F_neg[i-1]*v
            elif v == 0:
                F_pos[i], F_neg[i] = 0, 0
            else:
                F_neg[i] = min(0, F_pos[i-1]*v)
                F_pos[i] = max(0, F_neg[i-1]*v)

            maxa = max(maxa, F_pos[i])

        return maxa

    def maxProduct_error(self, A):
        
        if not A:
            return
        length = len(A)
        if length==1:
            return A[0]

        dp = [-1 for _ in xrange(length+1)]
        dp[length] = 0 
        for i in xrange(length-1, -1, -1):
            if A[i]<0:
                dp[i] = dp[i+1]+1
            elif A[i]==0:
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

        global_max = -1<<32
        
        
        
        
        
        

        cur = 0  
        for ind, val in enumerate(A):
            if cur!=0:
                cur *= val
            else:
                cur = val

            if cur<0 and dp[ind+1]<1:
                cur = 0

            global_max = max(global_max, cur)

        return global_max

    def maxProduct_dp(self, A):
        
        if not A:
            return
        length = len(A)
        if length==1:
            return A[0]

        dp = [-1 for _ in xrange(length+1)]
        dp[length] = 0 
        for i in xrange(length-1, -1, -1):
            if A[i]<0:
                dp[i] = dp[i+1]+1
            elif A[i]==0:
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

        global_max = -1<<32
        cur = 0  
        start_ptr = 0
        end_ptr = 0
        while end_ptr<length:  
            if cur!=0:
                cur *= A[end_ptr]
            else:
                cur = A[end_ptr]
                start_ptr = end_ptr

            end_ptr += 1

            if cur<0 and dp[end_ptr]<1:
                
                while start_ptr<=end_ptr and A[start_ptr]>0:
                    cur /= A[start_ptr]
                    start_ptr += 1
                if A[start_ptr]<0:
                    cur /= A[start_ptr]
                    start_ptr += 1
                if start_ptr==end_ptr:  
                    cur = 0 
                    
            global_max = max(global_max, cur)

        return global_max


if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""d""u""c""t""(""[""2"",""3"",""-""2"",""4""]"")""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""d""u""c""t""(""[""2"",""-""5"",""-""2"",""-""4"",""3""]"")""=""=""2""4""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""d""u""c""t""(""[""-""2"","" ""0"","" ""-""1""]"")""=""=""0""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""d""u""c""t""(""[""-""2""]"")""=""=""-""2""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""d""u""c""t""(""[""2"","" ""3"","" ""-""2"","" ""4"","" ""-""2""]"")""=""=""9""6""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""d""u""c""t""(""[""2"","" ""3"","" ""-""2"","" ""4"","" ""0"","" ""-""2""]"")""=""=""6""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""P""r""o""d""u""c""t""(""[""2"",""3"",""-""2"",""4""]"")""=""=""6""
