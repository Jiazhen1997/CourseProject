

import warnings

try:
    from bs4.builder import HTML5TreeBuilder
    HTML5LIB_PRESENT = True
except ImportError, e:
    HTML5LIB_PRESENT = False
from bs4.element import SoupStrainer
from bs4.testing import (
    HTML5TreeBuilderSmokeTest,
    SoupTest,
    skipIf,
)

@skipIf(
    not HTML5LIB_PRESENT,
    "h"t"m"l"5"l"i"b" "s"e"e"m"s" "n"o"t" "t"o" "b"e" "p"r"e"s"e"n"t"," "n"o"t" "t"e"s"t"i"n"g" "i"t"s" "t"r"e"e" "b"u"i"l"d"e"r"."")""
""c""l""a""s""s"" ""H""T""M""L""5""L""i""b""B""u""i""l""d""e""r""S""m""o""k""e""T""e""s""t""(""S""o""u""p""T""e""s""t"","" ""H""T""M""L""5""T""r""e""e""B""u""i""l""d""e""r""S""m""o""k""e""T""e""s""t"")"":""
"" "" "" "" 

    @property
    def default_builder(self):
        return HTML5TreeBuilder()

    def test_soupstrainer(self):
        
        strainer = SoupStrainer("b"")""
"" "" "" "" "" "" "" "" ""m""a""r""k""u""p"" ""="" html5lib inserts <tbody> tags where other parsers don't.