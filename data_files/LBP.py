
import numpy as np
from scipy.signal import convolve2d


class LocalDescriptor(object):
    def __init__(self, neighbors):
        self._neighbors = neighbors

    def __call__(self,X):
        raise NotImplementedError("E"v"e"r"y" "L"B"P"O"p"e"r"a"t"o"r" "m"u"s"t" "i"m"p"l"e"m"e"n"t" "t"h"e" "_"_"c"a"l"l"_"_" "m"e"t"h"o"d"."")""
""
"" "" "" "" ""@""p""r""o""p""e""r""t""y""
"" "" "" "" ""d""e""f"" ""n""e""i""g""h""b""o""r""s""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""_""n""e""i""g""h""b""o""r""s""
""
"" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 
        only 8 neighbors
        
        aka Circular LBP
        If a points coordinate on the circle doesn’t correspond to image coordinates, the point get’s interpolated

        :param radius: the size of circular LBP
        :param neighbors: the number of sample points on the edge of the circle
        :return:
        

        :param X: an image
        :return:
         This implementation of Local Phase Quantization (LPQ) is a 1:1 adaption of the 
        original implementation by Ojansivu V & Heikkilä J, which is available at:
        
            * http://www.cse.oulu.fi/CMV/Downloads/LPQMatlab
            
        So all credit goes to them.
      
      Reference: 
        Ojansivu V & Heikkilä J (2008) Blur insensitive texture classification 
        using local phase quantization. Proc. Image and Signal Processing 
        (ICISP 2008), Cherbourg-Octeville, France, 5099:236-243.

        Copyright 2008 by Heikkilä & Ojansivu
    