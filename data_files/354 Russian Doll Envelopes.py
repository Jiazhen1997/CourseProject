
import bisect

__author__ = 'Daniel'


class Solution(object):
    def maxEnvelopes(self, A):
        
        if not A: return 0

        A.sort(key=lambda (w, h): (w, -h))
        F = [-1 for _ in xrange(len(A)+1)]

        F[1] = A[0][1]  
        k = 1
        for _, h in A[1:]:
            idx = bisect.bisect_left(F, h, 1, k+1)
            F[idx] = h
            k += 1 if idx == k+1 else 0

        return k

    def maxEnvelopesTLE(self, A):
        
        if not A: return 0

        predicate = lambda a, b: b[0] > a[0] and b[1] > a[1]
        A.sort()
        n = len(A)
        F = [1 for _ in xrange(n)]
        for i in xrange(1, n):
            for j in xrange(i):
                if predicate(A[j], A[i]):
                    F[i] = max(F[i], 1 + F[j])

        return max(F)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""E""n""v""e""l""o""p""e""s""(""[""[""5"","" ""4""]"","" ""[""6"","" ""4""]"","" ""[""6"","" ""7""]"","" ""[""2"","" ""3""]""]"")"" ""=""="" ""3""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""m""a""x""E""n""v""e""l""o""p""e""s""(""[""[""2"",""1""0""0""]"",""[""3"",""2""0""0""]"",""[""4"",""3""0""0""]"",""[""5"",""5""0""0""]"",""[""5"",""4""0""0""]"",""[""5"",""2""5""0""]"",""[""6"",""3""7""0""]"",""[""6"",""3""6""0""]"",""[""7"",""3""8""0""]""]"")"" ""=""="" ""5""
