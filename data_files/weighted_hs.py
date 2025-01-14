from expr.feature import *

__author__ = 'Danyang'


class WeightedHS(SpatialHistogram):  
    def __init__(self, lbp_operator=ExtendedLBP(3), sz=(8, 8), X=None, y=None):
        super(WeightedHS, self).__init__(lbp_operator, sz)  
        self.weights = {}
        self.Hs = {}

        self.L = self.calculate_L(X)
        self.X = X
        self.y = y

    def init_cache(self):
        self.weights = {}
        self.Hs = {}

    def compute(self, X, y):
        raise NotImplementedError("N"o"t" "a"n"d" "w"o"n"'"t" "b"e" "i"m"p"l"e"m"e"n"t"e"d"."")""
""
"" "" "" "" ""d""e""f"" ""h""i""s""t""_""i""n""t""e""r""s""e""c""t""(""s""e""l""f"","" ""p"","" ""q"")"":""
"" "" "" "" "" "" "" "" ""p"" ""="" ""n""p"".""a""s""a""r""r""a""y""(""p"")"".""f""l""a""t""t""e""n""("")""
"" "" "" "" "" "" "" "" ""q"" ""="" ""n""p"".""a""s""a""r""r""a""y""(""q"")"".""f""l""a""t""t""e""n""("")""
"" "" "" "" "" "" "" "" ""s""i""m"" ""="" ""n""p"".""s""u""m""(""n""p"".""m""i""n""i""m""u""m""(""p"","" ""q"")"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""i""m""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""w""e""i""g""h""t""(""s""e""l""f"","" ""r""o""w"","" ""c""o""l"")"":""
"" "" "" "" "" "" "" "" ""a""r""g""s"" ""="" ""(""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" ""i""f"" ""a""r""g""s"" ""n""o""t"" ""i""n"" ""s""e""l""f"".""w""e""i""g""h""t""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""w""e""i""g""h""t""s""[""a""r""g""s""]"" ""="" ""s""e""l""f"".""_""g""e""t""_""w""e""i""g""h""t""(""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""w""e""i""g""h""t""s""[""a""r""g""s""]""
""
"" "" "" "" ""d""e""f"" ""_""g""e""t""_""w""e""i""g""h""t""(""s""e""l""f"","" ""r""o""w"","" ""c""o""l"")"":""
"" "" "" "" "" "" "" "" ""C"" ""="" ""l""e""n""(""n""p"".""u""n""i""q""u""e""(""s""e""l""f"".""y"")"")""
"" "" "" "" "" "" "" "" ""m""_""I"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""n""p"".""u""n""i""q""u""e""(""s""e""l""f"".""y"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""N""_""i"" ""="" ""s""e""l""f"".""g""e""t""_""N""(""i"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""H""s""_""i"" ""="" ""s""e""l""f"".""g""e""t""_""H""s""(""i"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""k"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""(""H""s""_""i"")"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""x""r""a""n""g""e""(""k"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""m""_""I"" ""+""="" ""s""e""l""f"".""h""i""s""t""_""i""n""t""e""r""s""e""c""t""(""H""s""_""i""[""j""]"","" ""H""s""_""i""[""k""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""_""I"" ""*""="" ""2"".""0""/""(""N""_""i""*""(""N""_""i""-""1"")"")""
"" "" "" "" "" "" "" "" ""m""_""I"" ""*""="" ""1"".""0""/""C""
""
"" "" "" "" "" "" "" "" ""S""2""_""I"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""n""p"".""u""n""i""q""u""e""(""s""e""l""f"".""y"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""H""s""_""i"" ""="" ""s""e""l""f"".""g""e""t""_""H""s""(""i"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""k"" ""i""n"" ""x""r""a""n""g""e""(""l""e""n""(""H""s""_""i"")"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""x""r""a""n""g""e""(""k"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""S""2""_""I"" ""+""="" ""(""s""e""l""f"".""h""i""s""t""_""i""n""t""e""r""s""e""c""t""(""H""s""_""i""[""j""]"","" ""H""s""_""i""[""k""]"")""-""m""_""I"")""*""*""2""
""
"" "" "" "" "" "" "" "" ""m""_""E"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""n""p"".""u""n""i""q""u""e""(""s""e""l""f"".""y"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""n""p"".""u""n""i""q""u""e""(""s""e""l""f"".""y""[""s""e""l""f"".""y"" ""!""="" ""i""]"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""N""_""i"" ""="" ""s""e""l""f"".""g""e""t""_""N""(""i"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""N""_""j"" ""="" ""s""e""l""f"".""g""e""t""_""N""(""j"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""H""s""_""i"" ""="" ""s""e""l""f"".""g""e""t""_""H""s""(""i"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""H""s""_""j"" ""="" ""s""e""l""f"".""g""e""t""_""H""s""(""j"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""h""_""i"" ""i""n"" ""H""s""_""i"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""h""_""j"" ""i""n"" ""H""s""_""j"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""m""_""E"" ""+""="" ""s""e""l""f"".""h""i""s""t""_""i""n""t""e""r""s""e""c""t""(""h""_""i"","" ""h""_""j"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""m""_""E"" ""*""="" ""1"".""0""/""(""N""_""i""*""N""_""j"")""
"" "" "" "" "" "" "" "" ""m""_""E"" ""*""="" ""2"".""0""/""(""C""*""(""C""-""1"")"")""
""
"" "" "" "" "" "" "" "" ""S""2""_""E"" ""="" ""0""
"" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""n""p"".""u""n""i""q""u""e""(""s""e""l""f"".""y"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""j"" ""i""n"" ""n""p"".""u""n""i""q""u""e""(""s""e""l""f"".""y""[""s""e""l""f"".""y""!""=""i""]"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""H""s""_""i"" ""="" ""s""e""l""f"".""g""e""t""_""H""s""(""i"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""H""s""_""j"" ""="" ""s""e""l""f"".""g""e""t""_""H""s""(""j"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""h""_""i"" ""i""n"" ""H""s""_""i"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""h""_""j"" ""i""n"" ""H""s""_""j"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""S""2""_""E"" ""+""="" ""(""s""e""l""f"".""h""i""s""t""_""i""n""t""e""r""s""e""c""t""(""h""_""i"","" ""h""_""j"")""-""m""_""E"")""*""*""2""
""
"" "" "" "" "" "" "" "" ""w""e""i""g""h""t"" ""="" ""(""m""_""I""-""m""_""E"")""*""*""2""/""(""S""2""_""I""+""S""2""_""E"")"" "" "" ""#"" ""h""i""s""t""o""g""r""a""m"" ""n""o""r""m""a""l""i""z""a""t""i""o""n"" ""w""o""n""'""t"" ""a""f""f""e""c""t"" ""w""e""i""g""h""t""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""w""e""i""g""h""t""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""N""(""s""e""l""f"","" ""i"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""l""e""n""(""s""e""l""f"".""X""[""s""e""l""f"".""y""=""=""i""]"")""
""
"" "" "" "" ""d""e""f"" ""c""a""l""c""u""l""a""t""e""_""L""(""s""e""l""f"","" ""X"")"":""
"" "" "" "" "" "" "" "" ""L"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""x"" ""i""n"" ""X"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""L"".""a""p""p""e""n""d""(""s""e""l""f"".""l""b""p""_""o""p""e""r""a""t""o""r""(""x"")"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""p"".""a""s""a""r""r""a""y""(""L"")""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""H""s""(""s""e""l""f"","" ""l""a""b""e""l"","" ""r""o""w"","" ""c""o""l"")"":""
"" "" "" "" "" "" "" "" ""a""r""g""s"" ""="" ""(""l""a""b""e""l"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" ""i""f"" ""a""r""g""s"" ""n""o""t"" ""i""n"" ""s""e""l""f"".""H""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""H""s""[""a""r""g""s""]"" ""="" ""s""e""l""f"".""_""g""e""t""_""H""s""(""l""a""b""e""l"","" ""r""o""w"","" ""c""o""l"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""H""s""[""a""r""g""s""]""
""
"" "" "" "" ""d""e""f"" ""_""g""e""t""_""H""s""(""s""e""l""f"","" ""l""a""b""e""l"","" ""r""o""w"","" ""c""o""l"")"":""
"" "" "" "" "" "" "" "" ""L"" ""="" ""s""e""l""f"".""L""[""s""e""l""f"".""y""=""=""l""a""b""e""l""]""
"" "" "" "" "" "" "" "" ""H""s"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""l"" ""i""n"" ""L"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""l""b""p""_""h""e""i""g""h""t"","" ""l""b""p""_""w""i""d""t""h"" ""="" ""l"".""s""h""a""p""e""
"" "" "" "" "" "" "" "" "" "" "" "" ""g""r""i""d""_""r""o""w""s"","" ""g""r""i""d""_""c""o""l""s"" ""="" ""s""e""l""f"".""s""z""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""y"" ""="" ""i""n""t""(""n""p"".""f""l""o""o""r""(""l""b""p""_""h""e""i""g""h""t"" ""/"" ""g""r""i""d""_""r""o""w""s"")"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""x"" ""="" ""i""n""t""(""n""p"".""f""l""o""o""r""(""l""b""p""_""w""i""d""t""h"" ""/"" ""g""r""i""d""_""c""o""l""s"")"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""C"" ""="" ""l""[""r""o""w"" ""*"" ""p""y"":""(""r""o""w"" ""+"" ""1"")"" ""*"" ""p""y"","" ""c""o""l"" ""*"" ""p""x"":""(""c""o""l"" ""+"" ""1"")"" ""*"" ""p""x""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""H""s"".""a""p""p""e""n""d""(""s""u""p""e""r""(""W""e""i""g""h""t""e""d""H""S"","" ""s""e""l""f"")"".""_""g""e""t""_""h""i""s""t""o""g""r""a""m""(""C"","" ""r""o""w"","" ""c""o""l"")"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""H""s""
""
"" "" "" "" ""d""e""f"" ""_""g""e""t""_""h""i""s""t""o""g""r""a""m""(""s""e""l""f"","" ""C"","" ""r""o""w"","" ""c""o""l"","" ""n""o""r""m""e""d""=""T""r""u""e"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""g""e""t""_""w""e""i""g""h""t""(""r""o""w"","" ""c""o""l"")""*"" ""\""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""u""p""e""r""(""W""e""i""g""h""t""e""d""H""S"","" ""s""e""l""f"")"".""_""g""e""t""_""h""i""s""t""o""g""r""a""m""(""C"","" ""r""o""w"","" ""c""o""l"")""
""
""
""c""l""a""s""s"" ""C""o""n""c""a""t""e""n""d""a""t""e""d""W""e""i""g""h""t""e""d""H""S""(""S""p""a""t""i""a""l""H""i""s""t""o""g""r""a""m"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""l""b""p""_""o""p""e""r""a""t""o""r""=""E""x""t""e""n""d""e""d""L""B""P""(""r""a""d""i""u""s""=""3"")"","" ""s""z""=""(""8"","" ""8"")"")"":""
"" "" "" "" "" "" "" "" ""s""u""p""e""r""(""C""o""n""c""a""t""e""n""d""a""t""e""d""W""e""i""g""h""t""e""d""H""S"","" ""s""e""l""f"")"".""_""_""i""n""i""t""_""_""(""l""b""p""_""o""p""e""r""a""t""o""r"","" ""s""z"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""w""e""i""g""h""t""s"" ""="" ""N""o""n""e""
""
"" "" "" "" ""d""e""f"" ""c""o""m""p""u""t""e""(""s""e""l""f"","" ""X"","" ""y"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""w""e""i""g""h""t""s"" ""="" ""s""e""l""f"".""c""o""n""s""t""r""u""c""t""_""w""i""g""h""t""s""(""X"","" ""y"")""
"" "" "" "" "" "" "" "" ""s""u""p""e""r""(""C""o""n""c""a""t""e""n""d""a""t""e""d""W""e""i""g""h""t""e""d""H""S"","" ""s""e""l""f"")"".""c""o""m""p""u""t""e""(""X"","" ""y"")""
""
"" "" "" "" ""d""e""f"" ""c""o""n""s""t""r""u""c""t""_""w""i""g""h""t""s""(""s""e""l""f"","" ""X"","" ""y"")"":""
"" "" "" "" "" "" "" "" ""X"" ""="" ""n""p"".""a""s""a""r""r""a""y""(""X"")""
"" "" "" "" "" "" "" "" ""n""_""g""a""b""o""r""s"" ""="" ""X"".""s""h""a""p""e""[""1""]""
""
"" "" "" "" "" "" "" "" ""w""e""i""g""h""t""s"" ""="" ""[""W""e""i""g""h""t""e""d""H""S""(""X""=""X""["":"","" ""i"","" "":"","" "":""]"","" ""y""=""y"")"" ""f""o""r"" ""i"" ""i""n"" ""x""r""a""n""g""e""(""n""_""g""a""b""o""r""s"")""]"" "" ""#"" ""m""a""n""i""p""u""l""a""t""e"" ""h""i""g""h"" ""d""i""m""e""n""s""i""o""n""a""l"" ""d""a""t""a""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""w""e""i""g""h""t""s""
""
"" "" "" "" ""d""e""f"" ""s""p""a""t""i""a""l""l""y""_""e""n""h""a""n""c""e""d""_""h""i""s""t""o""g""r""a""m""(""s""e""l""f"","" ""X"")"":""
"" "" "" "" "" "" "" "" ""h""i""s""t""s"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""g""a""b""o""r""_""i""d""x"","" ""x"" ""i""n"" ""e""n""u""m""e""r""a""t""e""(""X"")"":"" "" ""#"" ""r""e""d""u""c""e"" ""1"" ""d""i""m""e""n""s""i""o""n"","" ""g""a""b""o""r"" ""d""i""m""e""n""s""i""o""n""
"" "" "" "" "" "" "" "" "" "" "" "" ""h""i""s""t"" ""="" ""s""e""l""f"".""w""e""i""g""h""t""s""[""g""a""b""o""r""_""i""d""x""]"".""s""p""a""t""i""a""l""l""y""_""e""n""h""a""n""c""e""d""_""h""i""s""t""o""g""r""a""m""(""x"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""h""i""s""t""s"".""e""x""t""e""n""d""(""h""i""s""t"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""n""p"".""a""s""a""r""r""a""y""(""h""i""s""t""s"")""
""
""
""c""l""a""s""s"" ""W""e""i""g""h""t""e""d""L""G""B""P""H""S""(""C""h""a""i""n""e""d""F""e""a""t""u""r""e"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""n""_""o""r""i""e""n""t""=""4"","" ""n""_""s""c""a""l""e""=""2"","" ""l""b""p""_""o""p""e""r""a""t""o""r""=""E""x""t""e""n""d""e""d""L""B""P""(""r""a""d""i""u""s""=""3"")"")"":"" "" ""#"" ""a""l""t""e""r""n""a""t""i""v""e""l""y"" ""L""P""Q""
"" "" "" "" "" "" "" "" ""#"" ""T""O""D""O"" ""s""p""e""e""d"" ""u""p""
"" "" "" "" "" "" "" "" ""g""a""b""o""r"" ""="" ""G""a""b""o""r""F""i""l""t""e""r""C""v""2""(""n""_""o""r""i""e""n""t"","" ""n""_""s""c""a""l""e"")""
"" "" "" "" "" "" "" "" ""l""b""p""_""h""i""s""t"" ""="" ""C""o""n""c""a""t""e""n""d""a""t""e""d""W""e""i""g""h""t""e""d""H""S""(""l""b""p""_""o""p""e""r""a""t""o""r""=""l""b""p""_""o""p""e""r""a""t""o""r"")""
"" "" "" "" "" "" "" "" ""s""u""p""e""r""(""W""e""i""g""h""t""e""d""L""G""B""P""H""S"","" ""s""e""l""f"")"".""_""_""i""n""i""t""_""_""(""g""a""b""o""r"","" ""l""b""p""_""h""i""s""t"")""
