


import logging
import unittest
import sys
from bs4 import (
    BeautifulSoup,
    BeautifulStoneSoup,
)
from bs4.element import (
    CharsetMetaAttributeValue,
    ContentMetaAttributeValue,
    SoupStrainer,
    NamespacedAttribute,
    )
import bs4.dammit
from bs4.dammit import EntitySubstitution, UnicodeDammit
from bs4.testing import (
    SoupTest,
    skipIf,
)
import warnings

try:
    from bs4.builder import LXMLTreeBuilder, LXMLTreeBuilderForXML
    LXML_PRESENT = True
except ImportError, e:
    LXML_PRESENT = False

PYTHON_2_PRE_2_7 = (sys.version_info < (2,7))
PYTHON_3_PRE_3_2 = (sys.version_info[0] == 3 and sys.version_info < (3,2))

class TestDeprecatedConstructorArguments(SoupTest):

    def test_parseOnlyThese_renamed_to_parse_only(self):
        with warnings.catch_warnings(record=True) as w:
            soup = self.soup("<"a">"<"b">"<"/"b">"<"/"a">"","" ""p""a""r""s""e""O""n""l""y""T""h""e""s""e""=""S""o""u""p""S""t""r""a""i""n""e""r""(Standalone tests of the EntitySubstitution class.There's no need to do this except inside attribute values.Standalone tests of Unicode, Dammit.<foo>''""<"/"f"o"o">\357\273\277<?xml version="1"."0"" ""e""n""c""o""d""i""n""g""=
        chardet = bs4.dammit.chardet_dammit
        logging.disable(logging.WARNING)
        try:
            def noop(str):
                return None
            bs4.dammit.chardet_dammit = noop
            dammit = UnicodeDammit(doc)
            self.assertEqual(True, dammit.contains_replacement_characters)
            self.assertTrue(u"\"u"f"f"f"d"" ""i""n"" ""d""a""m""m""i""t"".""u""n""i""c""o""d""e""_""m""a""r""k""u""p"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""o""u""p"" ""="" ""B""e""a""u""t""i""f""u""l""S""o""u""p""(""d""o""c"","" 