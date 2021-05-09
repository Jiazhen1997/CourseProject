from facerec_py.facerec.classifier import SVM
from facerec_py.facerec.validation import KFoldCrossValidation
from facerec_py.facerec.model import PredictableModel
from svmutil import *
from itertools import product
import numpy as np
import logging


def range_f(begin, end, step):
    seq = []
    while True:
        if step == 0: break
        if step > 0 and begin > end: break
        if step < 0 and begin < end: break
        seq.append(begin)
        begin = begin + step
    return seq


def grid(grid_parameters):
    grid = []
    for parameter in grid_parameters:
        begin, end, step = parameter
        grid.append(range_f(begin, end, step))
    return product(*grid)


def grid_search(model, X, y, C_range=(-5,  15, 2), gamma_range=(3, -15, -2), k=5, num_cores=1):
    
    if not isinstance(model, PredictableModel):
        raise TypeError("G"r"i"d"S"e"a"r"c"h" "e"x"p"e"c"t"s" "a" "P"r"e"d"i"c"t"a"b"l"e"M"o"d"e"l"." "I"f" "y"o"u" "w"a"n"t" "t"o" "p"e"r"f"o"r"m" "o"p"t"i"m"i"z"a"t"i"o"n" "o"n" "r"a"w" "d"a"t"a" "u"s"e" "f"a"c"e"r"e"c"."f"e"a"t"u"r"e"."I"d"e"n"t"i"t"y" "t"o" "p"a"s"s" "u"n"p"r"e"p"r"o"c"e"s"s"e"d" "d"a"t"a"!"")""
"" "" "" "" ""i""f"" ""n""o""t"" ""i""s""i""n""s""t""a""n""c""e""(""m""o""d""e""l"".""c""l""a""s""s""i""f""i""e""r"","" ""S""V""M"")"":""
"" "" "" "" "" "" "" "" ""r""a""i""s""e"" ""T""y""p""e""E""r""r""o""r""(