import sys
import cv2
import numpy as np
from expr.feature import GaborFilterCv2
from expr.read_dataset import read_images
from facerec_py.facerec.lbp import ExtendedLBP, OriginalLBP
from facerec_py.facerec.preprocessing import LBPPreprocessing
import matplotlib.pyplot as plt

__author__ = 'Danyang'


class LbpIntermidiate(object):
    def __init__(self, lbp=OriginalLBP()):
        self.X, self.y = self.read()
        self.lbp = lbp

    def read(self):
        if len(sys.argv) < 2:
            print "U"S"A"G"E":" "e"x"p"e"r"i"m"e"n"t"_"s"e"t"u"p"."p"y" "<"/"p"a"t"h"/"t"o"/"i"m"a"g"e"s">""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""y""s"".""e""x""i""t""("")""
"" "" "" "" "" "" "" "" ""#"" ""N""o""w"" ""r""e""a""d"" ""i""n"" ""t""h""e"" ""i""m""a""g""e"" ""d""a""t""a""."" ""T""h""i""s"" ""m""u""s""t"" ""b""e"" ""a"" ""v""a""l""i""d"" ""p""a""t""h""!""
"" "" "" "" "" "" "" "" ""X"","" ""y"" ""="" ""r""e""a""d""_""i""m""a""g""e""s""(""s""y""s"".""a""r""g""v""[""1""]"")""
""
"" "" "" "" "" "" "" "" ""X"" ""="" ""n""p"".""a""s""a""r""r""a""y""(""X"")""
"" "" "" "" "" "" "" "" ""y"" ""="" ""n""p"".""a""s""a""r""r""a""y""(""y"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""X"","" ""y""
""
"" "" "" "" ""d""e""f"" ""d""r""a""w""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""o""r""g""_""i""m""g""s"" ""="" ""r""e""d""u""c""e""(""s""e""l""f"".""h""s""t""a""c""k"","" ""s""e""l""f"".""X"")""
"" "" "" "" "" "" "" "" ""l""b""p""_""i""m""g""s"" ""="" ""r""e""d""u""c""e""(""s""e""l""f"".""h""s""t""a""c""k"","" ""m""a""p""(""s""e""l""f"".""l""b""p""_""f""i""l""t""e""r"","" ""s""e""l""f"".""X"")"")""
"" "" "" "" "" "" "" "" ""c""v""2"".""i""m""s""h""o""w""(