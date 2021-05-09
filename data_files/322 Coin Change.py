
import sys

__author__ = 'Daniel'


class Solution(object):
    def coinChange(self, coins, amount):
        
        if amount == 0:
            return 0

        F = [sys.maxint for _ in xrange(amount+1)]
        for k in coins:
            if k < amount+1:
                F[k] = 1

        for i in xrange(1, amount+1):
            if F[i] != sys.maxint:
                for k in coins:
                    if i+k <= amount:
                        F[i+k] = min(F[i+k], F[i]+1)

        return F[amount] if F[amount] != sys.maxint else -1


class SolutionTLE(object):
    def coinChange(self, coins, amount):
        
        F = [sys.maxint for _ in xrange(amount+1)]
        for k in coins:
            if k < amount + 1:
                F[k] = 1

        for i in xrange(1, amount+1):
            for k in coins:
                if i-k > 0 and F[i-k] != sys.maxint:
                    F[i] = min(F[i], F[i-k]+1)

        return F[amount] if F[amount] != sys.maxint else -1


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""a""s""s""e""r""t"" ""S""o""l""u""t""i""o""n""("")"".""c""o""i""n""C""h""a""n""g""e""(""[""2""4""3"","" ""2""9""1"","" ""3""3""5"","" ""2""0""9"","" ""1""7""7"","" ""3""4""5"","" ""1""1""4"","" ""9""1"","" ""3""1""3"","" ""3""3""1""]"","" ""7""3""6""7"")"" ""=""="" ""2""3