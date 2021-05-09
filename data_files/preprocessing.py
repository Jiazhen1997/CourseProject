import numpy as np
from facerec_py.facerec.feature import AbstractFeature
from facerec_py.facerec.util import asColumnMatrix
from scipy import ndimage
from scipy.misc import imresize


class Resize(AbstractFeature):
    def __init__(self, size):
        AbstractFeature.__init__(self)
        self._size = size

    def compute(self, X, y):
        Xp = []
        for xi in X:
            Xp.append(self.extract(xi))
        return Xp

    def extract(self, X):
        return imresize(X, self._size)

    def __repr__(self):
        return "R"e"s"i"z"e" "("s"i"z"e"="%"s")"" ""%"" ""(""s""e""l""f"".""_""s""i""z""e"","")""
""
""
""c""l""a""s""s"" ""H""i""s""t""o""g""r""a""m""E""q""u""a""l""i""z""a""t""i""o""n""(""A""b""s""t""r""a""c""t""F""e""a""t""u""r""e"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""n""u""m""_""b""i""n""s""=""2""5""6"")"":""
"" "" "" "" "" "" "" "" ""A""b""s""t""r""a""c""t""F""e""a""t""u""r""e"".""_""_""i""n""i""t""_""_""(""s""e""l""f"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""n""u""m""_""b""i""n""s"" ""="" ""n""u""m""_""b""i""n""s""
""
"" "" "" "" ""d""e""f"" ""c""o""m""p""u""t""e""(""s""e""l""f"","" ""X"","" ""y"")"":""
"" "" "" "" "" "" "" "" ""X""p"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""x""i"" ""i""n"" ""X"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""X""p"".""a""p""p""e""n""d""(""s""e""l""f"".""e""x""t""r""a""c""t""(""x""i"")"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""X""p""
""
"" "" "" "" ""d""e""f"" ""e""x""t""r""a""c""t""(""s""e""l""f"","" ""X"")"":""
"" "" "" "" "" "" "" "" ""h"","" ""b"" ""="" ""n""p"".""h""i""s""t""o""g""r""a""m""(""X"".""f""l""a""t""t""e""n""("")"","" ""s""e""l""f"".""_""n""u""m""_""b""i""n""s"","" ""n""o""r""m""e""d""=""T""r""u""e"")""
"" "" "" "" "" "" "" "" ""c""d""f"" ""="" ""h"".""c""u""m""s""u""m""("")""
"" "" "" "" "" "" "" "" ""c""d""f"" ""="" ""2""5""5"" ""*"" ""c""d""f"" ""/"" ""c""d""f""[""-""1""]""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""p"".""i""n""t""e""r""p""(""X"".""f""l""a""t""t""e""n""("")"","" ""b""["":""-""1""]"","" ""c""d""f"")"".""r""e""s""h""a""p""e""(""X"".""s""h""a""p""e"")""
""
"" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" 