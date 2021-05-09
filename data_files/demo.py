
__author__ = 'Daniel'


from multiprocessing import Pool

from multiprocessing.dummy import Pool
from concurrent.futures import ProcessPoolExecutor


def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def threading():
    
    numbers = [(1963309, 2265973), (2030677, 3814172),
               (1551645, 2229620), (2039045, 2020802)]
    pool = ProcessPoolExecutor(max_workers=2)
    ret = list(pool.map(gcd, numbers))
    return ret
