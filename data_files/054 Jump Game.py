
__author__ = 'Danyang'
class Solution:
    def canJump_TLE(self, A):
        
        length = len(A)
        dp = [set([index]) for index in range(length)]

        for ind, val in enumerate(A):
            if ind!=0 and len(dp[ind])<2:
                continue

            
            for i in xrange(ind+1, ind+val+1):
                if i>=length:
                    break
                for item in dp[ind]:
                    dp[i].add(item)

        return 0 in dp[-1]

    def canJump_TLE2(self, A):
        
        l = len(A)
        dp = [False for _ in xrange(l+1)]  
        dp[0] = True
        for ind, val in enumerate(A):
            if dp[ind]:
                for i in xrange(1, val+1):  
                    if ind+i<l+1:
                        dp[ind+i] = True
                    else:
                        break
        return dp[-1]

    def canJump(self, A):
        
        l = len(A)
        
        if l<=1:
            return True

        
        dp = [-1 for _ in xrange(l)]  

        dp[0] = A[0]+0  
        for i in xrange(1, l):
            
            
            if dp[i-1]>=l-1:  
                return True

            
            if dp[i-1]<i:
                return False

            
            dp[i] = max(dp[i-1], A[i]+i)  

        return False



if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""J""u""m""p""(""[""2"","" ""3"","" ""1"","" ""1"","" ""4""]"")""=""=""T""r""u""e""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""a""n""J""u""m""p""(""[""3"","" ""2"","" ""1"","" ""0"","" ""4""]"")""=""=""F""a""l""s""e""
