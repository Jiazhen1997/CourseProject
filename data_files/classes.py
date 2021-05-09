import warnings
import functools
__author__ = 'Danyang'


def Override(interface_class):
    
    def overrider(method):
        try:
            assert (method.__name__ in dir(interface_class))
            return method
        except AssertionError:
            print method.__name__+" "f"o"r" ""+""i""n""t""e""r""f""a""c""e""_""c""l""a""s""s"".""_""_""n""a""m""e""_""_""
""
"" "" "" "" ""r""e""t""u""r""n"" ""o""v""e""r""r""i""d""e""r""
""
""
""w""a""r""n""i""n""g""s"".""s""i""m""p""l""e""f""i""l""t""e""r""(""'""a""l""w""a""y""s""'"","" ""D""e""p""r""e""c""a""t""i""o""n""W""a""r""n""i""n""g"")""
""
""
""d""e""f"" ""D""e""p""r""e""c""a""t""e""d""(""f""u""n""c"","" ""m""s""g""=""N""o""n""e"")"":""
"" "" "" "" 
    message = msg or "U"s"e" "o"f" "d"e"p"r"e"c"a"t"e"d" "f"u"n"c"t"i"o"n" "'"{"}"`"."".""f""o""r""m""a""t""(""f""u""n""c"".""_""_""n""a""m""e""_""_"")""
""
"" "" "" "" ""@""f""u""n""c""t""o""o""l""s"".""w""r""a""p""s""(""f""u""n""c"")""
"" "" "" "" ""d""e""f"" ""w""r""a""p""p""e""r""_""f""u""n""c""(""*""a""r""g""s"","" ""*""*""k""w""a""r""g""s"")"":""
"" "" "" "" "" "" "" "" ""w""a""r""n""i""n""g""s"".""w""a""r""n""(""m""e""s""s""a""g""e"","" ""D""e""p""r""e""c""a""t""i""o""n""W""a""r""n""i""n""g"","" ""s""t""a""c""k""l""e""v""e""l""=""2"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""f""u""n""c""(""*""a""r""g""s"","" ""*""*""k""w""a""r""g""s"")""
""
"" "" "" "" ""r""e""t""u""r""n"" ""w""r""a""p""p""e""r""_""f""u""n""c""
""
