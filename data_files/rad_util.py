



















__author__ = 'Tim Wegener <twegener@radlogic.com.au>'
__date__ = '$Date: 2007/03/27 03:15:06 $'
__version__ = '$Revision: 0.45 $'
__credits__ = 

import re
import sys
import time
import random

try:
    True, False
except NameError:
    True, False = (1==1, 0==1)


def int2bin(i, n):
    
    hex2bin = {'0': '0000', '1': '0001', '2': '0010', '3': '0011',
               '4': '0100', '5': '0101', '6': '0110', '7': '0111',
               '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
               'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111'}
    
    result = ''.join([hex2bin[x] for x in hex(i).lower().replace('l','')[2:]])
                      
    
    
    if '1' in result[:-n]:
        raise ValueError("V"a"l"u"e" "t"o"o" "l"a"r"g"e" "f"o"r" "g"i"v"e"n" "n"u"m"b"e"r" "o"f" "b"i"t"s"."")""
"" "" "" "" ""r""e""s""u""l""t"" ""="" ""r""e""s""u""l""t""[""-""n"":""]""
"" "" "" "" ""#"" ""Z""e""r""o""-""p""a""d"" ""i""f"" ""l""e""n""g""t""h"" ""l""o""n""g""e""r"" ""t""h""a""n"" ""m""a""p""p""e""d"" ""r""e""s""u""l""t"".""
"" "" "" "" ""r""e""s""u""l""t"" ""="" ""'""0""'""*""(""n""-""l""e""n""(""r""e""s""u""l""t"")"")"" ""+"" ""r""e""s""u""l""t""
"" "" "" "" ""r""e""t""u""r""n"" ""r""e""s""u""l""t""
""
""
""d""e""f"" ""b""i""n""2""i""n""t""(""b""i""n""_""s""t""r""i""n""g"")"":""
"" "" "" "" 










    return int(bin_string, 2)


def reverse(input_string):
    
    str_list = list(input_string)
    str_list.reverse()
    return ''.join(str_list)


def transpose(matrix):
    
    result = zip(*matrix)
    
    
    
    result = map(list, result)
    return result


def polygon_area(points_list, precision=100):
    
    
    for i in range(len(points_list)):
        points_list[i] = (int(points_list[i][0] * precision),
                          int(points_list[i][1] * precision))
    
    if points_list[-1] != points_list[0]:
        points_list.append(points_list[0])
    
    area = 0
    for i in range(len(points_list)-1):
        (x_i, y_i) = points_list[i]
        (x_i_plus_1, y_i_plus_1) = points_list[i+1]
        area = area + (x_i_plus_1 * y_i) - (y_i_plus_1 * x_i)
    area = abs(area / 2)
    
    area = float(area)/(precision**2)
    return area


def timestamp():
    

    return time.asctime()


def pt2str(point):
    
    return "("%"s"," "%"s")"" ""%"" ""(""s""t""r""(""p""o""i""n""t""[""0""]"")"","" ""s""t""r""(""p""o""i""n""t""[""1""]"")"")""
""
""
""d""e""f"" ""g""c""f""(""a"","" ""b"","" ""e""p""s""i""l""o""n""=""1""e""-""1""6"")"":""
"" "" "" "" 
    result = max(a, b)
    remainder = min(a, b)
    while remainder and abs(remainder) > epsilon:
        new_remainder = result % remainder
        result = remainder
        remainder = new_remainder
    return abs(result)

def lcm(a, b, precision=None):
    
    
    
    
    denom = gcf(a, b)
    if denom == 0:
        result = 0
    else:
        result = a * (b / denom)
    return result


def permutations(input_list):
    
    out_lists = []
    if len(input_list) > 1:
        
        item = input_list[0]
        
        sub_lists = permutations(input_list[1:])
        
        for sub_list in sub_lists:
            
            for i in range(len(input_list)):
                new_list = sub_list[:]
                new_list.insert(i, item)
                out_lists.append(new_list)
    else:
        
        out_lists = [input_list]
    return out_lists


def reduce_fraction(fraction):
    
    (numerator, denominator) = fraction
    common_factor = abs(gcf(numerator, denominator))
    result = (numerator/common_factor, denominator/common_factor)
    return result


def quantile(l, p):
    
    l_sort = l[:]
    l_sort.sort()
    n = len(l)
    r = 1 + ((n - 1) * p)
    i = int(r)
    f = r - i
    if i < n:
        result =  (1-f)*l_sort[i-1] + f*l_sort[i]
    else:
        result = l_sort[i-1]
    return result


def trim(l):
    
    l_sort = l[:]
    l_sort.sort()
    
    if len(l_sort) % 2 == 0:
        
        index = int(len(l_sort) / 2)  
        median = float(l_sort[index] + l_sort[index-1]) / 2
    else:
        
        index = int(len(l_sort) / 2)
        median = l_sort[index]
    
    q1 = quantile(l_sort, 0.25)
    q3 = quantile(l_sort, 0.75)
    iqr = q3 - q1
    iqr_extra = iqr * 1.5
    def in_interval(x, i=iqr_extra, q1=q1, q3=q3):
        return (x >= q1-i and x <= q3+i)
    l_trimmed = [x for x in l_sort if in_interval(x)]
    return l_trimmed


def nice_units(value, dp=0, sigfigs=None, suffix='', space=' ',
               use_extra_prefixes=False, use_full_name=False, mode='si'):
    
    si_prefixes = {1e24:  ('Y', 'yotta'),
                   1e21:  ('Z', 'zetta'),
                   1e18:  ('E', 'exa'),
                   1e15:  ('P', 'peta'),
                   1e12:  ('T', 'tera'),
                   1e9:   ('G', 'giga'),
                   1e6:   ('M', 'mega'),
                   1e3:   ('k', 'kilo'),
                   1e-3:  ('m', 'milli'),
                   1e-6:  ('u', 'micro'),
                   1e-9:  ('n', 'nano'),
                   1e-12: ('p', 'pico'),
                   1e-15: ('f', 'femto'),
                   1e-18: ('a', 'atto'),
                   1e-21: ('z', 'zepto'),
                   1e-24: ('y', 'yocto')
                   }
    if use_extra_prefixes:
        si_prefixes.update({1e2:  ('h', 'hecto'),
                            1e1:  ('da', 'deka'),
                            1e-1: ('d', 'deci'),
                            1e-2: ('c', 'centi')
                            })
    bin_prefixes = {2**10: ('K', 'kilo'),
                    2**20: ('M', 'mega'),
                    2**30: ('G', 'mega'),
                    2**40: ('T', 'tera'),
                    2**50: ('P', 'peta'),
                    2**60: ('E', 'exa')
                    }
    if mode == 'bin':
        prefixes = bin_prefixes
    else:
        prefixes = si_prefixes
    prefixes[1] = ('', '')  
    
    multipliers = prefixes.keys()
    multipliers.sort()
    mult = None
    for i in range(len(multipliers) - 1):
        lower_mult = multipliers[i]
        upper_mult = multipliers[i+1]
        if lower_mult <= value < upper_mult:
            mult_i = i
            break
    if mult is None:
        if value < multipliers[0]:
            mult_i = 0
        elif value >= multipliers[-1]:
            mult_i = len(multipliers) - 1
    mult = multipliers[mult_i]
    
    new_value = value / mult
    
    if sigfigs is None:
        if mult_i < (len(multipliers) - 1) and \
               round(new_value, dp) == \
               round((multipliers[mult_i+1] / mult), dp):
            mult = multipliers[mult_i + 1]
            new_value = value / mult
    
    if use_full_name:
        label_type = 1
    else:
        label_type = 0
    
    if sigfigs is None:
        str_value = eval('"%.'+str(dp)+'f" "%" "n"e"w"_"v"a"l"u"e"'"," "l"o"c"a"l"s"(")"," "{"}")"
" " " " "e"l"s"e":"
" " " " " " " " "s"t"r"_"v"a"l"u"e" "=" "e"v"a"l"("'""%"".""'""+""s""t""r""(""s""i""g""f""i""g""s"")""+""'""gReturn sequence with duplicate items in sequence seq removed.

    The code is based on usenet post by Tim Peters.

    This code is O(N) if the sequence items are hashable, O(N**2) if not.
    
    Peter Bengtsson has a blog post with an empirical comparison of other
    approaches:
    http://www.peterbe.com/plog/uniqifiers-benchmark

    If order is not important and the sequence items are hashable then
    list(set(seq)) is readable and efficient.

    If order is important and the sequence items are hashable generator
    expressions can be used (in py >= 2.4) (useful for large sequences):
    seen = set()
    do_something(x for x in seq if x not in seen or seen.add(x))

    Arguments:
    seq -- sequence
    preserve_order -- if not set the order will be arbitrary
                      Using this option will incur a speed penalty.
                      (default: False)

    Example showing order preservation:

    >>> uniquify(['a', 'aa', 'b', 'b', 'ccc', 'ccc', 'd'], preserve_order=True)
    ['a', 'aa', 'b', 'ccc', 'd']

    Example using a sequence of un-hashable items:

    >>> uniquify([['z'], ['x'], ['y'], ['z']], preserve_order=True)
    [['z'], ['x'], ['y']]

    The sorted output or the non-order-preserving approach should equal
    that of the sorted order-preserving approach output:
    
    >>> unordered = uniquify([3, 3, 1, 2], preserve_order=False)
    >>> unordered.sort()
    >>> ordered = uniquify([3, 3, 1, 2], preserve_order=True)
    >>> ordered.sort()
    >>> ordered
    [1, 2, 3]
    >>> int(ordered == unordered)
    1

    Reverse a dictionary so the items become the keys and vice-versa.

    Note: The results will be arbitrary if the items are not unique.

    >>> d = reverse_dict({'a': 1, 'b': 2})
    >>> d_items = d.items()
    >>> d_items.sort()
    >>> d_items
    [(1, 'a'), (2, 'b')]

    Return the n least significant bits of x.

    >>> lsb(13, 3)
    5

    Gray encode the given integer.Generate a random binary vector of length bits and given max value.Return a list of all possible binary numbers in order with width=bits. 
    
    It would be nice to extend it to match the
    functionality of python's range() built-in function.
    
    Return a list containing an arithmetic progression of floats.

    Return a list of floats between 0.0 (or start) and stop with an
    increment of step. 

    This is in functionality to python's range() built-in function 
    but can accept float increments.

    As with range(), stop is omitted from the list.

    Find common (prefix, suffix) of two strings.

    >>> find_common_fixes('abc', 'def')
    ('', '')

    >>> find_common_fixes('abcelephantdef', 'abccowdef')
    ('abc', 'def')

    >>> find_common_fixes('abcelephantdef', 'abccow')
    ('abc', '')

    >>> find_common_fixes('elephantdef', 'abccowdef')
    ('', 'def')

    Return true if the first sequence is a rotation of the second sequence.

    >>> seq1 = ['A', 'B', 'C', 'D']
    >>> seq2 = ['C', 'D', 'A', 'B']
    >>> int(is_rotated(seq1, seq2))
    1

    >>> seq2 = ['C', 'D', 'B', 'A']
    >>> int(is_rotated(seq1, seq2))
    0

    >>> seq1 = ['A', 'B', 'C', 'A']
    >>> seq2 = ['A', 'A', 'B', 'C']
    >>> int(is_rotated(seq1, seq2))
    1

    >>> seq2 = ['A', 'B', 'C', 'A']
    >>> int(is_rotated(seq1, seq2))
    1

    >>> seq2 = ['A', 'A', 'C', 'B']
    >>> int(is_rotated(seq1, seq2))
    0

    Return the module that contains the object definition of obj.

    Note: Use inspect.getmodule instead.

    Arguments:
    obj -- python obj, generally a class or a function

    Examples:
    
    A function:
    >>> module = getmodule(random.choice)
    >>> module.__name__
    'random'
    >>> module is random
    1

    A class:
    >>> module = getmodule(random.Random)
    >>> module.__name__
    'random'
    >>> module is random
    1

    A class inheriting from a class in another module:
    (note: The inheriting class must define at least one function.)
    >>> class MyRandom(random.Random):
    ...     def play(self):
    ...         pass
    >>> module = getmodule(MyRandom)
    >>> if __name__ == '__main__':
    ...     name = 'rad_util'
    ... else:
    ...     name = module.__name__
    >>> name
    'rad_util'
    >>> module is sys.modules[__name__]
    1

    Discussion:
    This approach is slightly hackish, and won't work in various situations.
    However, this was the approach recommended by GvR, so it's as good as
    you'll get.

    See GvR's post in this thread:
    http://groups.google.com.au/group/comp.lang.python/browse_thread/thread/966a7bdee07e3b34/c3cab3f41ea84236?lnk=st&q=python+determine+class+module&rnum=4&hl=en
    
    Round off the given value to the given grid size.

    Arguments:
    value -- value to be roudne
    grid -- result must be a multiple of this
    mode -- 0 nearest, 1 up, -1 down

    Examples:
    
    >>> round_grid(7.5, 5)
    10

    >>> round_grid(7.5, 5, mode=-1)
    5

    >>> round_grid(7.3, 5, mode=1)
    10

    >>> round_grid(7.3, 5.0, mode=1)
    10.0

    Store command-line args in a dictionary.
    
    -, -- prefixes are removed
    Items not prefixed with - or -- are stored as a list, indexed by 'args'

    For options that take a value use --option=value

    Consider using optparse or getopt (in Python standard library) instead.

    