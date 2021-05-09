
import bisect

__author__ = 'Daniel'


class Solution(object):
    def lengthOfLIS(self, A):
        
        if not A:
            return 0

        n = len(A)
        MIN = [-1 for _ in xrange(n+1)]
        k = 1
        MIN[k] = A[0]  
        for v in A[1:]:
            idx = bisect.bisect_left(MIN, v, 1, k+1)
            MIN[idx] = v
            k += 1 if idx == k+1 else 0

        return k

    def bin_search(self, M, A, t, lo=0, hi=None):
        if not hi: hi = len(M)
        while lo < hi:
            m = (lo+hi)/2
            if A[M[m]] == t:
                return m
            elif A[M[m]] < t:
                lo = m + 1
            else:
                hi = m

        return lo

    def lengthOfLIS_output_all(self, A):
        
        if not A:
            return 0

        n = len(A)
        MIN = [-1 for _ in xrange(n+1)]
        RET = [-1 for _ in xrange(n)]
        l = 1
        MIN[l] = 0
        for i in xrange(1, n):
            if A[i] > A[MIN[l]]:
                l += 1
                MIN[l] = i

                RET[i] = MIN[l-1]  
            else:
                j = self.bin_search(MIN, A, A[i], 1, l+1)
                MIN[j] = i

                RET[i] = MIN[j-1] if j-1 >= 1 else -1  

        
        cur = MIN[l]
        ret = []
        while True:
            ret.append(A[cur])
            if RET[cur] == -1: break
            cur = RET[cur]

        ret = ret[::-1]
        print ret

        return l

    def lengthOfLIS_dp(self, A):
        
        if not A:
            return 0

        n = len(A)
        F = [1 for _ in xrange(n)]
        maxa = 1
        for i in xrange(1, n):
            F[i] = max(
                F[j] + 1 if A[i] > A[j] else 1
                for j in xrange(i)
            )
            maxa = max(maxa, F[i])

        return maxa


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""l""e""n""g""t""h""O""f""L""I""S""(""[""1""0"","" ""9"","" ""2"","" ""5"","" ""3"","" ""7"","" ""1""0""1"","" ""1""8""]"")"" ""=""="" ""4