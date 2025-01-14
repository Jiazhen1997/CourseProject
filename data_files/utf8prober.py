


























from . import constants
from .charsetprober import CharSetProber
from .codingstatemachine import CodingStateMachine
from .mbcssm import UTF8SMModel

ONE_CHAR_PROB = 0.5


class UTF8Prober(CharSetProber):
    def __init__(self):
        CharSetProber.__init__(self)
        self._mCodingSM = CodingStateMachine(UTF8SMModel)
        self.reset()

    def reset(self):
        CharSetProber.reset(self)
        self._mCodingSM.reset()
        self._mNumOfMBChar = 0

    def get_charset_name(self):
        return "u"t"f"-"8""
""
"" "" "" "" ""d""e""f"" ""f""e""e""d""(""s""e""l""f"","" ""a""B""u""f"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""c"" ""i""n"" ""a""B""u""f"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""d""i""n""g""S""t""a""t""e"" ""="" ""s""e""l""f"".""_""m""C""o""d""i""n""g""S""M"".""n""e""x""t""_""s""t""a""t""e""(""c"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""c""o""d""i""n""g""S""t""a""t""e"" ""=""="" ""c""o""n""s""t""a""n""t""s"".""e""E""r""r""o""r"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""m""S""t""a""t""e"" ""="" ""c""o""n""s""t""a""n""t""s"".""e""N""o""t""M""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""b""r""e""a""k""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""c""o""d""i""n""g""S""t""a""t""e"" ""=""="" ""c""o""n""s""t""a""n""t""s"".""e""I""t""s""M""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""m""S""t""a""t""e"" ""="" ""c""o""n""s""t""a""n""t""s"".""e""F""o""u""n""d""I""t""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""b""r""e""a""k""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""c""o""d""i""n""g""S""t""a""t""e"" ""=""="" ""c""o""n""s""t""a""n""t""s"".""e""S""t""a""r""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""_""m""C""o""d""i""n""g""S""M"".""g""e""t""_""c""u""r""r""e""n""t""_""c""h""a""r""l""e""n""("")"" "">""="" ""2"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""m""N""u""m""O""f""M""B""C""h""a""r"" ""+""="" ""1""
""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""g""e""t""_""s""t""a""t""e""("")"" ""=""="" ""c""o""n""s""t""a""n""t""s"".""e""D""e""t""e""c""t""i""n""g"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""g""e""t""_""c""o""n""f""i""d""e""n""c""e""("")"" "">"" ""c""o""n""s""t""a""n""t""s"".""S""H""O""R""T""C""U""T""_""T""H""R""E""S""H""O""L""D"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""_""m""S""t""a""t""e"" ""="" ""c""o""n""s""t""a""n""t""s"".""e""F""o""u""n""d""I""t""
""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""g""e""t""_""s""t""a""t""e""("")""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""c""o""n""f""i""d""e""n""c""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""u""n""l""i""k""e"" ""="" ""0"".""9""9""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""_""m""N""u""m""O""f""M""B""C""h""a""r"" ""<"" ""6"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""i"" ""i""n"" ""r""a""n""g""e""(""0"","" ""s""e""l""f"".""_""m""N""u""m""O""f""M""B""C""h""a""r"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""u""n""l""i""k""e"" ""="" ""u""n""l""i""k""e"" ""*"" ""O""N""E""_""C""H""A""R""_""P""R""O""B""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""1"".""0"" ""-"" ""u""n""l""i""k""e""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""u""n""l""i""k""e""
