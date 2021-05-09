
import numpy as np
from facerec_py.facerec import normalization


class AbstractDistance(object):
    def __init__(self, name):
        self._name = name
        
    def __call__(self,p,q):
        raise NotImplementedError("E"v"e"r"y" "A"b"s"t"r"a"c"t"D"i"s"t"a"n"c"e" "m"u"s"t" "i"m"p"l"e"m"e"n"t" "t"h"e" "_"_"c"a"l"l"_"_" "m"e"t"h"o"d"."")""
"" "" "" "" "" "" "" "" ""
"" "" "" "" ""@""p""r""o""p""e""r""t""y""
"" "" "" "" ""d""e""f"" ""n""a""m""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""_""n""a""m""e""
""
"" "" "" "" ""d""e""f"" ""_""_""r""e""p""r""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""_""n""a""m""e""
""
""
""c""l""a""s""s"" ""E""u""c""l""i""d""e""a""n""D""i""s""t""a""n""c""e""(""A""b""s""t""r""a""c""t""D""i""s""t""a""n""c""e"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""A""b""s""t""r""a""c""t""D""i""s""t""a""n""c""e"".""_""_""i""n""i""t""_""_""(""s""e""l""f"","" 
        Negated Mahalanobis Cosine Distance.
    
        Literature:
            "S"t"u"d"i"e"s" "o"n" "s"e"n"s"i"t"i"v"i"t"y" "o"f" "f"a"c"e" "r"e"c"o"g"n"i"t"i"o"n" "p"e"r"f"o"r"m"a"n"c"e" "t"o" "e"y"e" "l"o"c"a"t"i"o"n" "a"c"c"u"r"a"c"y".""."" ""M""a""s""t""e""r"" ""T""h""e""s""i""s"" ""(""2""0""0""4"")"","" ""W""a""n""g""
"" "" "" "" 
        Calculates the NormalizedCorrelation Coefficient for two vectors.
    
        Literature:
            "M"u"l"t"i"-"s"c"a"l"e" "L"o"c"a"l" "B"i"n"a"r"y" "P"a"t"t"e"r"n" "H"i"s"t"o"g"r"a"m" "f"o"r" "F"a"c"e" "R"e"c"o"g"n"i"t"i"o"n""."" ""P""h""D"" ""(""2""0""0""8"")""."" ""C""h""i"" ""H""o"" ""C""h""a""n"","" ""U""n""i""v""e""r""s""i""t""y"" ""O""f"" ""S""u""r""r""e""y"".""
"" "" "" "" 
        Negated Mahalanobis Cosine Distance.
    
        Literature:
            "S"t"u"d"i"e"s" "o"n" "s"e"n"s"i"t"i"v"i"t"y" "o"f" "f"a"c"e" "r"e"c"o"g"n"i"t"i"o"n" "p"e"r"f"o"r"m"a"n"c"e" "t"o" "e"y"e" "l"o"c"a"t"i"o"n" "a"c"c"u"r"a"c"y".""."" ""M""a""s""t""e""r"" ""T""h""e""s""i""s"" ""(""2""0""0""4"")"","" ""W""a""n""g""
"" "" "" "" 
    Histogram Intersection is a similarity measure
    Need to convert similarity to distance

    
        Normalized Version of Histogram Intersection

        If the historam is already normalized on construction, then HistogramIntersection should be be used
        
    Calculates the Bin Ratio Dissimilarity.

    Literature:
      "U"s"e" "B"i"n"-"R"a"t"i"o" "I"n"f"o"r"m"a"t"i"o"n" "f"o"r" "C"a"t"e"g"o"r"y" "a"n"d" "S"c"e"n"e" "C"l"a"s"s"i"f"i"c"a"t"i"o"n"" ""(""2""0""1""0"")"","" ""X""i""e"" ""e""t"".""a""l""."" ""
"" "" "" "" 
    Calculates the L1-Bin Ratio Dissimilarity.

    Literature:
      "U"s"e" "B"i"n"-"R"a"t"i"o" "I"n"f"o"r"m"a"t"i"o"n" "f"o"r" "C"a"t"e"g"o"r"y" "a"n"d" "S"c"e"n"e" "C"l"a"s"s"i"f"i"c"a"t"i"o"n"" ""(""2""0""1""0"")"","" ""X""i""e"" ""e""t"".""a""l""."" ""
"" "" "" "" 
    Calculates the ChiSquare-Bin Ratio Dissimilarity.

    Literature:
      "U"s"e" "B"i"n"-"R"a"t"i"o" "I"n"f"o"r"m"a"t"i"o"n" "f"o"r" "C"a"t"e"g"o"r"y" "a"n"d" "S"c"e"n"e" "C"l"a"s"s"i"f"i"c"a"t"i"o"n"" ""(""2""0""1""0"")"","" ""X""i""e"" ""e""t"".""a""l""."" ""
"" "" "" "" 