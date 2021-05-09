

import unittest

from bs4 import BeautifulSoup
from bs4.builder import (
    builder_registry as registry,
    HTMLParserTreeBuilder,
    TreeBuilderRegistry,
)

try:
    from bs4.builder import HTML5TreeBuilder
    HTML5LIB_PRESENT = True
except ImportError:
    HTML5LIB_PRESENT = False

try:
    from bs4.builder import (
        LXMLTreeBuilderForXML,
        LXMLTreeBuilder,
        )
    LXML_PRESENT = True
except ImportError:
    LXML_PRESENT = False


class BuiltInRegistryTest(unittest.TestCase):
    

    def test_combination(self):
        if LXML_PRESENT:
            self.assertEqual(registry.lookup('fast', 'html'),
                             LXMLTreeBuilder)

        if LXML_PRESENT:
            self.assertEqual(registry.lookup('permissive', 'xml'),
                             LXMLTreeBuilderForXML)
        self.assertEqual(registry.lookup('strict', 'html'),
                          HTMLParserTreeBuilder)
        if HTML5LIB_PRESENT:
            self.assertEqual(registry.lookup('html5lib', 'html'),
                              HTML5TreeBuilder)

    def test_lookup_by_markup_type(self):
        if LXML_PRESENT:
            self.assertEqual(registry.lookup('html'), LXMLTreeBuilder)
            self.assertEqual(registry.lookup('xml'), LXMLTreeBuilderForXML)
        else:
            self.assertEqual(registry.lookup('xml'), None)
            if HTML5LIB_PRESENT:
                self.assertEqual(registry.lookup('html'), HTML5TreeBuilder)
            else:
                self.assertEqual(registry.lookup('html'), HTMLParserTreeBuilder)

    def test_named_library(self):
        if LXML_PRESENT:
            self.assertEqual(registry.lookup('lxml', 'xml'),
                             LXMLTreeBuilderForXML)
            self.assertEqual(registry.lookup('lxml', 'html'),
                             LXMLTreeBuilder)
        if HTML5LIB_PRESENT:
            self.assertEqual(registry.lookup('html5lib'),
                              HTML5TreeBuilder)

        self.assertEqual(registry.lookup('html.parser'),
                          HTMLParserTreeBuilder)

    def test_beautifulsoup_constructor_does_lookup(self):
        
        BeautifulSoup("","" ""f""e""a""t""u""r""e""s""=Test the TreeBuilderRegistry class in general.