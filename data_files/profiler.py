from cProfile import Profile
from pstats import Stats


__author__ = 'Daniel'


def demo():
    
    f = lambda x: x

    profiler = Profile()
    profiler.runcall(f)  

    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    
    stats.print_stats()

    
    
    
    stats.print_callers()
    stats.print_callees()
