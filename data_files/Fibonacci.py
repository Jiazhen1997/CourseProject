
__author__ = 'Daniel'


class Solution:
    def fibonacci(self, n):
        
        f = lambda n: reduce(lambda x, n: [x[1], x[0]+x[1]], range(n), [0, 1])[0]  
        return f(n-1)