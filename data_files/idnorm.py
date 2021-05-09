




from __future__ import with_statement

import sys
import re

DEBUG = True

class Annotation(object):
    def __init__(self, id_, type_):
        self.id_ = id_
        self.type_ = type_

    def map_ids(self, idmap):
        self.id_ = idmap[self.id_]

class Textbound(Annotation):
    def __init__(self, id_, type_, offsets, text):
        Annotation.__init__(self, id_, type_)
        self.offsets = offsets
        self.text = text

    def map_ids(self, idmap):
        Annotation.map_ids(self, idmap)

    def __str__(self):
        return "%"s"\"t"%"s" "%"s"\"t"%"s"" ""%"" ""(""s""e""l""f"".""i""d""_"","" ""s""e""l""f"".""t""y""p""e""_"","" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'"" ""'"".""j""o""i""n""(""s""e""l""f"".""o""f""f""s""e""t""s"")"","" ""s""e""l""f"".""t""e""x""t"")""
""c""l""a""s""s"" ""A""r""g""A""n""n""o""t""a""t""i""o""n""(""A""n""n""o""t""a""t""i""o""n"")"":""
"" "" "" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""i""d""_"","" ""t""y""p""e""_"","" ""a""r""g""s"")"":""
"" "" "" "" "" "" "" "" ""A""n""n""o""t""a""t""i""o""n"".""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""i""d""_"","" ""t""y""p""e""_"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""r""g""s"" ""="" ""a""r""g""s""
""
"" "" "" "" ""d""e""f"" ""m""a""p""_""i""d""s""(""s""e""l""f"","" ""i""d""m""a""p"")"":""
"" "" "" "" "" "" "" "" ""A""n""n""o""t""a""t""i""o""n"".""m""a""p""_""i""d""s""(""s""e""l""f"","" ""i""d""m""a""p"")""
"" "" "" "" "" "" "" "" ""m""a""p""p""e""d"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""a""r""g"" ""i""n"" ""s""e""l""f"".""a""r""g""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""k""e""y"","" ""v""a""l""u""e"" ""="" ""a""r""g"".""s""p""l""i""t""(""'"":""'"")"" ""
"" "" "" "" "" "" "" "" "" "" "" "" ""v""a""l""u""e"" ""="" ""i""d""m""a""p""[""v""a""l""u""e""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""m""a""p""p""e""d"".""a""p""p""e""n""d""(