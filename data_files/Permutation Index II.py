
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def permutationIndexII(self, A):
        
        idx = 0
        factor = 1
        cnt = defaultdict(int)

        cnt[A[-1]] += 1
        n = len(A)
        for i in xrange(n-2, -1, -1):
            cnt[A[i]] += 1  
            for k, v in cnt.items():
                if k < A[i]:
                    idx += v * factor / cnt[A[i]]

            factor = factor * (n-i) / cnt[A[i]]

        return idx+1

if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""S""o""l""u""t""i""o""n""("")"".""p""e""r""m""u""t""a""t""i""o""n""I""n""d""e""x""I""I""(""[""1"","" ""4"","" ""2"","" ""2""]"")""
