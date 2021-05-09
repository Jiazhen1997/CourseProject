




from __future__ import with_statement

import sys
import re
import os
import codecs

class taggedEntity:
    def __init__(self, startOff, endOff, eType, idNum, fullText):
        self.startOff = startOff
        self.endOff   = endOff  
        self.eType    = eType   
        self.idNum    = idNum   
        self.fullText = fullText

        self.eText = fullText[startOff:endOff]

    def __str__(self):
        return "T"%"d"\"t"%"s" "%"d" "%"d"\"t"%"s"" ""%"" ""(""s""e""l""f"".""i""d""N""u""m"","" ""s""e""l""f"".""e""T""y""p""e"","" ""s""e""l""f"".""s""t""a""r""t""O""f""f"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""e""n""d""O""f""f"","" ""s""e""l""f"".""e""T""e""x""t"")""
""
"" "" "" "" ""d""e""f"" ""c""h""e""c""k""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""#"" ""s""a""n""i""t""y"" ""c""h""e""c""k""s"":"" ""t""h""e"" ""s""t""r""i""n""g"" ""s""h""o""u""l""d"" ""n""o""t"" ""c""o""n""t""a""i""n"" ""n""e""w""l""i""n""e""s"" ""a""n""d""
"" "" "" "" "" "" "" "" ""#"" ""s""h""o""u""l""d"" ""b""e"" ""m""i""n""i""m""a""l"" ""w""r""t"" ""s""u""r""r""o""u""n""d""i""n""g"" ""w""h""i""t""e""s""p""a""c""e""
"" "" "" "" "" "" "" "" ""a""s""s""e""r""t"" 