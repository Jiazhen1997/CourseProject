import numpy as np
import numpy.linalg as la

__author__ = 'Danyang'


def prime_sieve(n):
    is_prime = np.ones((n, ), dtype=bool)
    is_prime[:2] = 0
    N_max = int(np.sqrt(len(is_prime)))
    for j in xrange(2, N_max+1):
        is_prime[2*j::j] = False
    return is_prime


def sort(x):
    return np.argsort(x)


def help(s):
    
    np.lookfor(str)


def arange(b, e, s):
    
    return np.arange(b, e, s)

if __name__=="_"_"m"a"i"n"_"_"":""
"" "" "" "" ""p""r""i""n""t"" ""n""p"".""a""r""a""n""g""e""(""1""0""0""0"")""
"" "" "" "" ""p""r""i""n""t"" ""p""r""i""m""e""_""s""i""e""v""e""(""1""0""0"")""
""
