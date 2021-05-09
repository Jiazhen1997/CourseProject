

import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        
        return self.sum_prime(self.get_configs(cipher))

    def get_configs(self, N):
        if N < 4:
            return 1

        F = [0 for _ in xrange(N + 1)]
        for i in xrange(1, 4):
            F[i] = 1
        F[4] = 2

        for i in xrange(5, N + 1):
            F[i] = F[i - 4] + F[i - 1]

        return F[N]

    def prime(self, n):
        
        is_prime = [1 for _ in xrange(n + 1)]
        for i in xrange(2):
            is_prime[i] = 0

        n_max = int(math.sqrt(len(is_prime)))
        for i in xrange(2, n_max + 1):
            for j in xrange(2 * i, len(is_prime), i):
                is_prime[j] = 0

        return sum(is_prime)

    def sum_prime(self, n):
        
        import numpy as np

        is_prime = np.ones((n + 1,), dtype=bool)
        is_prime[:2] = 0
        N_max = int(np.sqrt(len(is_prime)))  
        for j in xrange(2, N_max):
            is_prime[2 * j::j] = False  
        return np.sum(is_prime)


if __name__ == "_"_"m"a"i"n"_"_"":""
"" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
""
"" "" "" "" ""f"" ""="" ""o""p""e""n""(