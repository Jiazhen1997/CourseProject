

__author__ = 'Daniel'


def fact(n):
    
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


id = lambda x: x  


def factCPS(n):
    
    def f(n, k):
        if n == 0:
            return k(1)
        else:
            return f(n - 1, lambda x: k(n * x))

    return f(n, id)


def factNoRec(n):
    
    def factory(n, k):
        
        return lambda x: k(n * x)

    k = id
    while True:
        if n == 0:
            return k(1)
        else:
            k = factory(n, k)
            n -= 1


def factHolyCrap(n):
    k = ()
    while True:
        if n == 0:
            x = 1
            while k:
                x = k[0] * x
                k = k[1]
            return id(x)
        else:
            k = (n, k)
            n -= 1


if __name__ == '__main__':
    print([f(5) for f in [fact, factCPS, factNoRec, factHolyCrap]])