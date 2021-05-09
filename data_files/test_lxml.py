

import re
import warnings

try:
    from bs4.builder import LXMLTreeBuilder, LXMLTreeBuilderForXML
    LXML_PRESENT = True
except ImportError, e:
    LXML_PRESENT = False

from bs4 import (
    BeautifulSoup,
    BeautifulStoneSoup,
    )
from bs4.element import Comment, Doctype, SoupStrainer
from bs4.testing import skipIf
from bs4.tests import test_htmlparser
from bs4.testing import (
    HTMLTreeBuilderSmokeTest,
    XMLTreeBuilderSmokeTest,
    SoupTest,
    skipIf,
)

@skipIf(
    not LXML_PRESENT,
    "l"x"m"l" "s"e"e"m"s" "n"o"t" "t"o" "b"e" "p"r"e"s"e"n"t"," "n"o"t" "t"e"s"t"i"n"g" "i"t"s" "t"r"e"e" "b"u"i"l"d"e"r"."")""
""c""l""a""s""s"" ""L""X""M""L""T""r""e""e""B""u""i""l""d""e""r""S""m""o""k""e""T""e""s""t""(""S""o""u""p""T""e""s""t"","" ""H""T""M""L""T""r""e""e""B""u""i""l""d""e""r""S""m""o""k""e""T""e""s""t"")"":""
"" "" "" "" 

    @property
    def default_builder(self):
        return LXMLTreeBuilder()

    def test_out_of_range_entity(self):
        self.assertSoupEquals(
            "<"p">"f"o"o"&"#"1"0"0"0"0"0"0"0"0"0"0"0"0"0";"b"a"r"<"/"p">"","" lxml strips the XML definition from an XHTML doc, which is fine.<?xml version="1"."0"" ""e""n""c""o""d""i""n""g""=
        soup = self.soup(markup)
        self.assertEqual(
            soup.encode("u"t"f"-"8"")"".""r""e""p""l""a""c""e""(""bSee ``HTMLTreeBuilderSmokeTest``.