
















from __future__ import generators

__version__ = '$Revision: 0.9 $'
__date__ = '$Date: 2007/03/27 04:15:26 $'
__credits__ = 


try:
    set
except NameError:
    from sets import Set as set

from rad_util import is_rotated


class CycleError(Exception):
    
    pass


def topsort(pairlist):
    
    num_parents = {}  
    children = {}  
    for parent, child in pairlist: 
        
        if not num_parents.has_key( parent ): 
            num_parents[parent] = 0 
        if not num_parents.has_key( child ): 
            num_parents[child] = 0 

        
        num_parents[child] += 1

        
        children.setdefault(parent, []).append(child)

    
    answer = [x for x in num_parents.keys() if num_parents[x] == 0]

    
    
    for parent in answer: 
        del num_parents[parent]
        if children.has_key( parent ): 
            for child in children[parent]: 
                num_parents[child] -= 1
                if num_parents[child] == 0: 
                    answer.append( child ) 
            
            
            del children[parent]

    if num_parents: 
        
        
        raise CycleError(answer, num_parents, children)
    return answer 

def topsort_levels(pairlist):
    
    num_parents = {}  
    children = {}  
    for parent, child in pairlist: 
        
        if not num_parents.has_key( parent ): 
            num_parents[parent] = 0 
        if not num_parents.has_key( child ): 
            num_parents[child] = 0 

        
        num_parents[child] += 1

        
        children.setdefault(parent, []).append(child)

    return topsort_levels_core(num_parents, children)

def topsort_levels_core(num_parents, children):
    
    while 1:
        
        level_parents = [x for x in num_parents.keys() if num_parents[x] == 0]

        if not level_parents:
            break

        
        
        yield level_parents

        
        
        
        for level_parent in level_parents:

            del num_parents[level_parent]

            if children.has_key(level_parent):
                for level_parent_child in children[level_parent]:
                    num_parents[level_parent_child] -= 1
                del children[level_parent]
        
    if num_parents: 
        
        
        raise CycleError(num_parents, children)
    else:
        
        raise StopIteration


def find_cycles(parent_children):
    
    cycles = []
    visited_nodes = set()

    for parent in parent_children:
        if parent in visited_nodes:
            
            continue

        paths = [[parent]]
        while paths:
            path = paths.pop()

            parent = path[-1]
            
            try:
                children = parent_children[parent]
            except KeyError:
                continue

            for child in children:
                
                
                
                
                if child in path:
                    
                    cycle = path[path.index(child):]
                    
                    is_dup = False
                    for other_cycle in cycles:
                        if is_rotated(other_cycle, cycle):
                            is_dup = True
                            break
                    if not is_dup:
                        cycles.append(cycle)
                        yield cycle
                else:
                    
                    
                    
                    paths.append(path + [child])
                    
                    visited_nodes.add(child)


if __name__ == '__main__':
    
    import sys
    import doctest
    doctest.testmod(sys.modules['__main__'])
