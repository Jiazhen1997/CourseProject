




import sys
import re
import os
import codecs


FIELDED_OUTPUT_RE = re.compile(r'^\d+\|')

class taggedEntity:
    def __init__(self, startOff, endOff, eType, idNum):
        self.startOff = startOff
        self.endOff   = endOff  
        self.eType    = eType   
        self.idNum    = idNum   

    def __str__(self):
        return "T"%"d"\"t"%"s" "%"d" "%"d"" ""%"" ""(""s""e""l""f"".""i""d""N""u""m"","" ""s""e""l""f"".""e""T""y""p""e"","" ""s""e""l""f"".""s""t""a""r""t""O""f""f"","" ""s""e""l""f"".""e""n""d""O""f""f"")""
""
""d""e""f"" ""M""e""t""a""M""a""p""_""l""i""n""e""s""_""t""o""_""s""t""a""n""d""o""f""f""(""m""e""t""a""m""a""p""_""l""i""n""e""s"","" ""r""e""f""t""e""x""t""=""N""o""n""e"")"":""
"" "" "" "" ""t""a""g""g""e""d"" ""="" ""[""]""
"" "" "" "" ""i""d""s""e""q"" ""="" ""1""
"" "" "" "" ""f""o""r"" ""l"" ""i""n"" ""m""e""t""a""m""a""p""_""l""i""n""e""s"":""
"" "" "" "" "" "" "" "" ""l"" ""="" ""l"".""r""s""t""r""i""p""(""'""\""n""'"")""
""
"" "" "" "" "" "" "" "" ""#"" ""s""i""l""e""n""t""l""y"" ""s""k""i""p"" ""l""i""n""e""s"" ""t""h""a""t"" ""d""o""n""'""t"" ""m""a""t""c""h"" ""t""h""e"" ""e""x""p""e""c""t""e""d"" ""f""o""r""m""a""t"" "" "" "" "" "" "" "" ""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""F""I""E""L""D""E""D""_""O""U""T""P""U""T""_""R""E"".""m""a""t""c""h""(""l"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""t""i""n""u""e""
"" "" "" "" "" "" "" "" ""
"" "" "" "" "" "" "" "" ""#"" ""f""o""r""m""a""t"" ""i""s"" ""p""i""p""e""-""s""e""p""a""r""a""t""e""d"" ""(