__author__ = 'Danyang'
def memoize(func):
    
    cache = {}
    def ret(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return ret


def memoize_force(func):
    
    cache = {}
    def ret(*args):
        k = str(args)
        if k not in cache:
            cache[k] = func(*args)
        return cache[k]
    return ret


def memoize_iterable(func):
    
    cache = {}
    def ret(*args):
        k = tuple(args)
        if k not in cache:
            cache[k] = func(*args)
        return cache[k]
    return ret