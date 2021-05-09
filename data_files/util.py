
import os
from PIL import Image
import numpy as np
import random


def read_image(filename):
    imarr = np.array([])
    try:
        im = Image.open(os.path.join(filename))
        im = im.convert("L"")"" "" ""#"" ""c""o""n""v""e""r""t"" ""t""o"" ""g""r""e""y""s""c""a""l""e""
"" "" "" "" "" "" "" "" ""i""m""a""r""r"" ""="" ""n""p"".""a""r""r""a""y""(""i""m"","" ""d""t""y""p""e""=""n""p"".""u""i""n""t""8"")""
"" "" "" "" ""e""x""c""e""p""t"" ""I""O""E""r""r""o""r"" ""a""s"" ""(""e""r""r""n""o"","" ""s""t""r""e""r""r""o""r"")"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" 
    Creates a row-matrix from multi-dimensional data items in list l.
    
    X [list] List with multi-dimensional data.
    
    Creates a column-matrix from multi-dimensional data items in list X.
    
    X [list] List with multi-dimensional data.
     min-max normalize a given matrix to given range [low,high].
    
    Args:
        X [rows x columns] input data
        low [numeric] lower bound
        high [numeric] upper bound
     Shuffles two arrays!
    

    :param row_vec: 1d np array
    :return:
    

    :param col_vec: 2d np array
    :return:
    