






from __future__ import with_statement

import sys
import re
import os
import codecs

def parse_id(l):
    m = re.match(r'^((\S)(\S*))', l)
    assert m, "F"a"i"l"e"d" "t"o" "p"a"r"s"e" "I"D":" "%"s"" ""%"" ""l""
"" "" "" "" ""r""e""t""u""r""n"" ""m"".""g""r""o""u""p""s""("")""
""
""d""e""f"" ""p""a""r""s""e""_""k""e""y""_""v""a""l""u""e""(""k""v"")"":""
"" "" "" "" ""m"" ""="" ""r""e"".""m""a""t""c""h""(""r""'""^""(""\""S""+"")"":""(""\""S""+"")""$""'"","" ""k""v"")""
"" "" "" "" ""a""s""s""e""r""t"" ""m"","" 