



























from .charsetprober import CharSetProber
from .constants import eNotMe
from .compat import wrap_ord

FREQ_CAT_NUM = 4

UDF = 0  
OTH = 1  
ASC = 2  
ASS = 3  
ACV = 4  
ACO = 5  
ASV = 6  
ASO = 7  
CLASS_NUM = 8  

Latin1_CharToClass = (
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, ASC, ASC, ASC, ASC, ASC, ASC, ASC,   
    ASC, ASC, ASC, ASC, ASC, ASC, ASC, ASC,   
    ASC, ASC, ASC, ASC, ASC, ASC, ASC, ASC,   
    ASC, ASC, ASC, OTH, OTH, OTH, OTH, OTH,   
    OTH, ASS, ASS, ASS, ASS, ASS, ASS, ASS,   
    ASS, ASS, ASS, ASS, ASS, ASS, ASS, ASS,   
    ASS, ASS, ASS, ASS, ASS, ASS, ASS, ASS,   
    ASS, ASS, ASS, OTH, OTH, OTH, OTH, OTH,   
    OTH, UDF, OTH, ASO, OTH, OTH, OTH, OTH,   
    OTH, OTH, ACO, OTH, ACO, UDF, ACO, UDF,   
    UDF, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, ASO, OTH, ASO, UDF, ASO, ACO,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    OTH, OTH, OTH, OTH, OTH, OTH, OTH, OTH,   
    ACV, ACV, ACV, ACV, ACV, ACV, ACO, ACO,   
    ACV, ACV, ACV, ACV, ACV, ACV, ACV, ACV,   
    ACO, ACO, ACV, ACV, ACV, ACV, ACV, OTH,   
    ACV, ACV, ACV, ACV, ACV, ACO, ACO, ACO,   
    ASV, ASV, ASV, ASV, ASV, ASV, ASO, ASO,   
    ASV, ASV, ASV, ASV, ASV, ASV, ASV, ASV,   
    ASO, ASO, ASV, ASV, ASV, ASV, ASV, OTH,   
    ASV, ASV, ASV, ASV, ASV, ASO, ASO, ASO,   
)





Latin1ClassModel = (
    
    0,  0,  0,  0,  0,  0,  0,  0,  
    0,  3,  3,  3,  3,  3,  3,  3,  
    0,  3,  3,  3,  3,  3,  3,  3,  
    0,  3,  3,  3,  1,  1,  3,  3,  
    0,  3,  3,  3,  1,  2,  1,  2,  
    0,  3,  3,  3,  3,  3,  3,  3,  
    0,  3,  1,  3,  1,  1,  1,  3,  
    0,  3,  1,  3,  1,  1,  3,  3,  
)


class Latin1Prober(CharSetProber):
    def __init__(self):
        CharSetProber.__init__(self)
        self.reset()

    def reset(self):
        self._mLastCharClass = OTH
        self._mFreqCounter = [0] * FREQ_CAT_NUM
        CharSetProber.reset(self)

    def get_charset_name(self):
        return "w"i"n"d"o"w"s"-"1"2"5"2""
""
"" "" "" "" ""d""e""f"" ""f""e""e""d""(""s""e""l""f"","" ""a""B""u""f"")"":""
"" "" "" "" "" "" "" "" ""a""B""u""f"" ""="" ""s""e""l""f"".""f""i""l""t""e""r""_""w""i""t""h""_""e""n""g""l""i""s""h""_""l""e""t""t""e""r""s""(""a""B""u""f"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""c"" ""i""n"" ""a""B""u""f"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""h""a""r""C""l""a""s""s"" ""="" ""L""a""t""i""n""1""_""C""h""a""r""T""o""C""l""a""s""s""[""w""r""a""p""_""o""r""d""(""c"")""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""r""e""q"" ""="" ""L""a""t""i""n""1""C""l""a""s""s""M""o""d""e""l""[""(""s""e""l""f"".""_""m""L""a""s""t""C""h""a""r""C""l""a""s""s"" ""*"" ""C""L""A""S""S""_""N""U""M"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""+"" ""c""h""a""r""C""l""a""s""s""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""f""r""e""q"" ""=""="" ""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""m""S""t""a""t""e"" ""="" ""e""N""o""t""M""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""b""r""e""a""k""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""m""F""r""e""q""C""o""u""n""t""e""r""[""f""r""e""q""]"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""m""L""a""s""t""C""h""a""r""C""l""a""s""s"" ""="" ""c""h""a""r""C""l""a""s""s""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""g""e""t""_""s""t""a""t""e""("")""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""c""o""n""f""i""d""e""n""c""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""g""e""t""_""s""t""a""t""e""("")"" ""=""="" ""e""N""o""t""M""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""0"".""0""1""
""
"" "" "" "" "" "" "" "" ""t""o""t""a""l"" ""="" ""s""u""m""(""s""e""l""f"".""_""m""F""r""e""q""C""o""u""n""t""e""r"")""
"" "" "" "" "" "" "" "" ""i""f"" ""t""o""t""a""l"" ""<"" ""0"".""0""1"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""f""i""d""e""n""c""e"" ""="" ""0"".""0""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""f""i""d""e""n""c""e"" ""="" ""(""(""s""e""l""f"".""_""m""F""r""e""q""C""o""u""n""t""e""r""[""3""]"" ""/"" ""t""o""t""a""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""-"" ""(""s""e""l""f"".""_""m""F""r""e""q""C""o""u""n""t""e""r""[""1""]"" ""*"" ""2""0"".""0"" ""/"" ""t""o""t""a""l"")"")""
"" "" "" "" "" "" "" "" ""i""f"" ""c""o""n""f""i""d""e""n""c""e"" ""<"" ""0"".""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""f""i""d""e""n""c""e"" ""="" ""0"".""0""
"" "" "" "" "" "" "" "" ""#"" ""l""o""w""e""r"" ""t""h""e"" ""c""o""n""f""i""d""e""n""c""e"" ""o""f"" ""l""a""t""i""n""1"" ""s""o"" ""t""h""a""t"" ""o""t""h""e""r"" ""m""o""r""e"" ""a""c""c""u""r""a""t""e""
"" "" "" "" "" "" "" "" ""#"" ""d""e""t""e""c""t""o""r"" ""c""a""n"" ""t""a""k""e"" ""p""r""i""o""r""i""t""y"".""
"" "" "" "" "" "" "" "" ""c""o""n""f""i""d""e""n""c""e"" ""="" ""c""o""n""f""i""d""e""n""c""e"" ""*"" ""0"".""5""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""c""o""n""f""i""d""e""n""c""e""
