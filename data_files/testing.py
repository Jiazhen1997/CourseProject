

import copy
import functools
import unittest
from unittest import TestCase
from bs4 import BeautifulSoup
from bs4.element import (
    CharsetMetaAttributeValue,
    Comment,
    ContentMetaAttributeValue,
    Doctype,
    SoupStrainer,
)

from bs4.builder import HTMLParserTreeBuilder
default_builder = HTMLParserTreeBuilder


class SoupTest(unittest.TestCase):

    @property
    def default_builder(self):
        return default_builder()

    def soup(self, markup, **kwargs):
        
        builder = kwargs.pop('builder', self.default_builder)
        return BeautifulSoup(markup, builder=builder, **kwargs)

    def document_for(self, markup):
        
        return self.default_builder.test_fragment_to_document(markup)

    def assertSoupEquals(self, to_parse, compare_parsed_to=None):
        builder = self.default_builder
        obj = BeautifulSoup(to_parse, builder=builder)
        if compare_parsed_to is None:
            compare_parsed_to = to_parse

        self.assertEqual(obj.decode(), self.document_for(compare_parsed_to))


class HTMLTreeBuilderSmokeTest(object):

    

    def assertDoctypeHandled(self, doctype_fragment):
        
        doctype_str, soup = self._document_with_doctype(doctype_fragment)

        
        doctype = soup.contents[0]
        self.assertEqual(doctype.__class__, Doctype)
        self.assertEqual(doctype, doctype_fragment)
        self.assertEqual(str(soup)[:len(doctype_str)], doctype_str)

        
        
        self.assertEqual(soup.p.contents[0], 'foo')

    def _document_with_doctype(self, doctype_fragment):
        
        doctype = '<!DOCTYPE %s>' % doctype_fragment
        markup = doctype + '\n<p>foo</p>'
        soup = self.soup(markup)
        return doctype, soup

    def test_normal_doctypes(self):
        
        self.assertDoctypeHandled("h"t"m"l"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""D""o""c""t""y""p""e""H""a""n""d""l""e""d""(""
"" "" "" "" "" "" "" "" "" "" "" "" ""'""h""t""m""l"" ""P""U""B""L""I""C"" A real XHTML document should come out more or less the same as it went in.<?xml version="1"."0"" ""e""n""c""o""d""i""n""g""=
        soup = self.soup(markup)
        self.assertEqual(
            soup.encode("u"t"f"-"8"")"".""r""e""p""l""a""c""e""(""bMake sure you can copy the tree builder.

        This is important because the builder is part of a
        BeautifulSoup object, and we want to be able to copy that.
        A <p> tag is never designated as an empty-element tag.

        Even if the markup shows it as an empty-element tag, it
        shouldn't be presented that way.
        A tag that's not closed by the end of the document should be closed.

        This applies to all tags except empty-element tags.
        A <br> tag is designated as an empty-element tag.

        Some parsers treat <br></br> as one <br/> tag, some parsers as
        two tags, but it should always be an empty-element tag.
        Whitespace must be preserved in <pre> and <textarea> tags.Inline elements can be nested indefinitely.Block elements can be nested.One table can go inside another one.Parsers don't need to *understand* namespaces, but at the
        very least they should not choke on namespaces or lose
        data.Parsers should be able to work with SoupStrainers.<foo attr='bar "b"r"a"w"l"s"" ""h""a""p""p""e""n""'"">""a""<""/""f""o""o""><foo attr='bar "b"r"a"w"l"s"" ""h""a""p""p""e""n""'"">""a""<""/""f""o""o""><foo attr="B"r"a"w"l"s" "h"a"p"p"e"n" "a"t" "&"q"u"o"t";"B"o"b"\"'"s" "B"a"r"&"q"u"o"t";"">""a""<""/""f""o""o"">A real XHTML document should come out *exactly* the same as it went in.<?xml version="1"."0"" ""e""n""c""o""d""i""n""g""=
        soup = self.soup(markup)
        self.assertEqual(
            soup.encode("u"t"f"-"8"")"","" ""m""a""r""k""u""p"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""p""o""p""p""i""n""g""_""n""a""m""e""s""p""a""c""e""d""_""t""a""g""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""m""a""r""k""u""p"" ""="" ""'""<""r""s""s"" ""x""m""l""n""s"":""d""c""=A large XML document should come out the same as it went in.Smoke test for a tree builder that supports HTML5.