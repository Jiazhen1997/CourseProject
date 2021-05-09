
__author__ = 'Daniel'


class Solution(object):
    def numWays_oneliner(self, n, k):
        return 0 if n < 1 else sum(reduce(lambda F, i: [(k-1)*(F[0]+F[1]), F[0]], xrange(1, n), [k, 0]))

    def numWays(self, n, k):
        
        if n < 1:
            return 0

        num_diff = k
        num_same = 0
        for _ in xrange(1, n):
            num_diff, num_same = (k-1)*(num_diff+num_same), num_diff

        return num_diff+num_same

    def numWays_MLE2(self, n, k):
        
        if n < 1:
            return 0

        F = [[[0 for _ in xrange(k)] for _ in xrange(k)] for _ in xrange(2)]
        EMPTY = 0

        for j0 in xrange(k):
            F[1][j0][EMPTY] = 1

        for i in xrange(2, n+1):
            for j0 in xrange(k):
                for j1 in xrange(k):
                    F[i%2][j0][j1] = 0

            for j0 in xrange(k):
                for j1 in xrange(k):
                    for j2 in xrange(k):
                        if i == 2:
                            F[i%2][j0][j1] = F[(i-1)%2][j1][EMPTY]

                        elif j1 == j2 and j0 != j1:
                            F[i%2][j0][j1] += F[(i-1)%2][j1][j2]
                        elif j1 != j2:
                            F[i%2][j0][j1] += F[(i-1)%2][j1][j2]

        ret = 0
        for j0 in xrange(k):
            for j1 in xrange(k):
                ret += F[n%2][j0][j1]

        return ret

    def numWays_MLE(self, n, k):
        
        if n < 1:
            return 0

        F = [[[0 for _ in xrange(k)] for _ in xrange(k)] for _ in xrange(n+1)]
        EMPTY = 0

        for j0 in xrange(k):
            F[1][j0][EMPTY] = 1

        for i in xrange(2, n+1):
            for j0 in xrange(k):
                for j1 in xrange(k):
                    for j2 in xrange(k):
                        if i == 2:
                            F[i][j0][j1] = F[i-1][j1][EMPTY]

                        elif j1 == j2 and j0 != j1:
                            F[i][j0][j1] += F[i-1][j1][j2]
                        elif j1 != j2:
                            F[i][j0][j1] += F[i-1][j1][j2]

        ret = 0
        for j0 in xrange(k):
            for j1 in xrange(k):
                ret += F[n][j0][j1]

        return ret


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""n""u""m""W""a""y""s""(""3"","" ""2"")"" ""=""="" ""6""
""
""
