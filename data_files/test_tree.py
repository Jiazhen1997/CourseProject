


import copy
import pickle
import re
import warnings
from bs4 import BeautifulSoup
from bs4.builder import (
    builder_registry,
    HTMLParserTreeBuilder,
)
from bs4.element import (
    CData,
    Doctype,
    NavigableString,
    SoupStrainer,
    Tag,
)
from bs4.testing import (
    SoupTest,
    skipIf,
)

XML_BUILDER_PRESENT = (builder_registry.lookup("x"m"l"")"" ""i""s"" ""n""o""t"" ""N""o""n""e"")""
""L""X""M""L""_""P""R""E""S""E""N""T"" ""="" ""(""b""u""i""l""d""e""r""_""r""e""g""i""s""t""r""y"".""l""o""o""k""u""p""(Make sure that the given tags have the correct text.

        This is used in tests that define a bunch of tags, each
        containing a single string, and then select certain strings by
        some mechanism.
        Make sure that the given tags have the correct IDs.

        This is used in tests that define a bunch of tags, each
        containing a single string, and then select certain strings by
        some mechanism.
        Basic tests of the find() method.

    find() just calls find_all() with limit=1, so it's not tested all
    that thouroughly here.
    Basic tests of the find_all() method.You can search the tree for text nodes.You can limit the number of items returned by find_all.Test ways of finding tags by tag name.<a>First tag.</a>
                                  <b>Second tag.</b>
                                  <c>Third <a>Nested tag.</a> tag.</c><a id="a"">""M""a""t""c""h"" ""1"".""<""/""a"">""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""<""a"" ""i""d""=)

        self.assertSelects(
            tree.find_all(id_matches_name), ["M"a"t"c"h" "1"."","" 
                         <a id="f"i"r"s"t"">""M""a""t""c""h""i""n""g"" ""a"".""<""/""a"">""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""<""a"" ""i""d""=)
        self.assertSelects(tree.find_all(id='first'),
                           ["M"a"t"c"h"i"n"g" "a"."","" 
                         <a name="n"a"m"e"1"" ""c""l""a""s""s""=)

        
        self.assertSelects(tree.find_all(name='name1'),
                           ["A" "t"a"g" "c"a"l"l"e"d" "'"n"a"m"e"1"'".""]"")""
"" "" "" "" "" "" "" "" ""#"" ""T""h""i""s"" ""d""o""e""s"" ""w""h""a""t"" ""y""o""u"" ""w""a""n""t"".""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""t""r""e""e"".""f""i""n""d""_""a""l""l""(""a""t""t""r""s""=""{""'""n""a""m""e""'"" "":"" ""'""n""a""m""e""1""'""}"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""[
                         <a class="1"">""C""l""a""s""s"" ""1"".""<""/""a"">""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""<""a"" ""c""l""a""s""s""=)

        
        
        self.assertSelects(tree.find_all('a', class_='1'), ['Class 1.'])
        self.assertSelects(tree.find_all('c', class_='3'), ['Class 3 and 4.'])
        self.assertSelects(tree.find_all('c', class_='4'), ['Class 3 and 4.'])

        
        self.assertSelects(tree.find_all('a', '1'), ['Class 1.'])
        self.assertSelects(tree.find_all(attrs='1'), ['Class 1.', 'Class 1.'])
        self.assertSelects(tree.find_all('c', '3'), ['Class 3 and 4.'])
        self.assertSelects(tree.find_all('c', '4'), ['Class 3 and 4.'])

    def test_find_by_class_when_multiple_classes_present(self):
        tree = self.soup("<"g"a"r" "c"l"a"s"s"="'"f"o"o" "b"a"r"'">"F"o"u"n"d" "i"t"<"/"g"a"r">"")""
""
"" "" "" "" "" "" "" "" ""f"" ""="" ""t""r""e""e"".""f""i""n""d""_""a""l""l""(
                         <a id="f"i"r"s"t"">""M""a""t""c""h"".""<""/""a"">""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""<""a"" ""i""d""=)

        strainer = SoupStrainer(attrs={'id' : 'first'})
        self.assertSelects(tree.find_all(strainer), ['Match.'])

    def test_find_all_with_missing_atribute(self):
        
        
        tree = self.soup()
        self.assertSelects(tree.find_all('a', id=None), ["N"o" "I"D" "p"r"e"s"e"n"t".""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""f""i""n""d""_""a""l""l""_""w""i""t""h""_""d""e""f""i""n""e""d""_""a""t""t""r""i""b""u""t""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""#"" ""Y""o""u"" ""c""a""n"" ""p""a""s""s"" ""i""n"" ""N""o""n""e"" ""a""s"" ""t""h""e"" ""v""a""l""u""e"" ""o""f"" ""a""n"" ""a""t""t""r""i""b""u""t""e"" ""t""o"" ""f""i""n""d""_""a""l""l"".""
"" "" "" "" "" "" "" "" ""#"" ""T""h""i""s"" ""w""i""l""l"" ""m""a""t""c""h"" ""t""a""g""s"" ""t""h""a""t"" ""h""a""v""e"" ""t""h""a""t"" ""a""t""t""r""i""b""u""t""e"" ""s""e""t"" ""t""o"" ""a""n""y"" ""v""a""l""u""e"".""
"" "" "" "" "" "" "" "" ""t""r""e""e"" ""="" ""s""e""l""f"".""s""o""u""p""()
        self.assertSelects(
            tree.find_all(id=True), ["I"D" "p"r"e"s"e"n"t"."","" <a id=1>Unquoted attribute.</a>
                            <a id="1"">""Q""u""o""t""e""d"" ""a""t""t""r""i""b""u""t""e"".""<""/""a""><a id="1"">""1""<""/""a"">""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""<""a"" ""i""d""=)
        self.assertSelects(tree.find_all(id=["1"","" <a id="a"">""O""n""e"" ""a"".""<""/""a"">""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""<""a"" ""i""d""=)

        self.assertSelects(tree.find_all(id=re.compile("^"a"+"$"")"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""[Test Tag.index<div>
                            <a>Identical</a>
                            <b>Not identical</b>
                            <a>Identical</a>

                            <c><d>Identical with child</d></c>
                            <b>Also not identical</b>
                            <c><d>Identical with child</d></c>
                            </div>Test navigation and searching through an element's parents.Test the ability to create new tags.<p id="1"">""D""o""n""'""t"" ""l""e""a""v""e"" ""m""e"" ""<""b"">""h""e""r""e""<""/""b"">"".""<""/""p"">""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""<""p"" ""i""d""=
        soup = self.soup(doc)
        second_para = soup.find(id='2')
        bold = soup.b

        
        soup.find(id='2').append(soup.b)

        
        self.assertEqual(bold.parent, second_para)

        self.assertEqual(
            soup.decode(), self.document_for(
                '<p id="1"">""D""o""n""\""'""t"" ""l""e""a""v""e"" ""m""e"" "".""<""/""p"">""\""n""'""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'""<""p"" ""i""d""=<a>We<b>reserve<c>the</c><d>right</d></b></a><e>to<f>refuse</f><g>service</g></e>
            <p>Unneeded <em>formatting</em> is unneeded</p>
            Tag.clear()Tag.string = 'string'"""
"" "" "" "" "" "" "" "" ""s""o""u""p"" ""="" ""s""e""l""f"".""s""o""u""p""(Test various features of element objects.The length of an element is its number of children.Accessing a Python member .foo invokes find('foo')has_attr() checks for the presence of an attribute.

        Please note note: has_attr() is different from
        __in__. has_attr() checks the tag's attributes and __in__
        checks the tag's chidlren.
        Only a tag containing a single text node has a .string.Tag.text and Tag.get_text(sep=u"")"" ""-"">"" ""a""l""l"" ""c""h""i""l""d"" ""t""e""x""t"","" ""c""o""n""c""a""t""e""n""a""t""e""dTesting cdata-list attributes like 'class'.
    <!DOCTYPE HTML PUBLIC "-"/"/"W"3"C"/"/"D"T"D" "H"T"M"L" "4"."0" "T"r"a"n"s"i"t"i"o"n"a"l"/"/"E"N""

        self.tree = self.soup(self.page)

    def test_pickle_and_unpickle_identity(self):
        
        
        dumped = pickle.dumps(self.tree, 2)
        loaded = pickle.loads(dumped)
        self.assertEqual(loaded.__class__, BeautifulSoup)
        self.assertEqual(loaded.decode(), self.tree.decode())

    def test_deepcopy_identity(self):
        
        copied = copy.deepcopy(self.tree)
        self.assertEqual(copied.decode(), self.tree.decode())

    def test_unicode_pickle(self):
        
        html = u"<"b">"\"N"{"S"N"O"W"M"A"N"}"<"/"b">""
"" "" "" "" "" "" "" "" ""s""o""u""p"" ""="" ""s""e""l""f"".""s""o""u""p""(""h""t""m""l"")""
"" "" "" "" "" "" "" "" ""d""u""m""p""e""d"" ""="" ""p""i""c""k""l""e"".""d""u""m""p""s""(""s""o""u""p"","" ""p""i""c""k""l""e"".""H""I""G""H""E""S""T""_""P""R""O""T""O""C""O""L"")""
"" "" "" "" "" "" "" "" ""l""o""a""d""e""d"" ""="" ""p""i""c""k""l""e"".""l""o""a""d""s""(""d""u""m""p""e""d"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""o""a""d""e""d"".""d""e""c""o""d""e""("")"","" ""s""o""u""p"".""d""e""c""o""d""e""("")"")""
""
""
""c""l""a""s""s"" ""T""e""s""t""S""u""b""s""t""i""t""u""t""i""o""n""s""(""S""o""u""p""T""e""s""t"")"":""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""d""e""f""a""u""l""t""_""f""o""r""m""a""t""t""e""r""_""i""s""_""m""i""n""i""m""a""l""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""m""a""r""k""u""p"" ""="" ""uTest the ability to encode objects into strings.Text inside a CData object is passed into the formatter.

        But the return value is ignored.
        
<!DOCTYPE HTML PUBLIC "-"/"/"W"3"C"/"/"D"T"D" "H"T"M"L" "4"."0"1"/"/"E"N""


    def setUp(self):
        self.soup = BeautifulSoup(self.HTML)

    def assertSelects(self, selector, expected_ids):
        el_ids = [el['id'] for el in self.soup.select(selector)]
        el_ids.sort()
        expected_ids.sort()
        self.assertEqual(expected_ids, el_ids,
            "S"e"l"e"c"t"o"r" "%"s"," "e"x"p"e"c"t"e"d" "["%"s"]"," "g"o"t" "["%"s"]"" ""%"" ""(""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""e""c""t""o""r"","" ""'"","" ""'"".""j""o""i""n""(""e""x""p""e""c""t""e""d""_""i""d""s"")"","" ""'"","" ""'"".""j""o""i""n""(""e""l""_""i""d""s"")""
"" "" "" "" "" "" "" "" "" "" "" "" "")""
"" "" "" "" "" "" "" "" "")""
""
"" "" "" "" ""a""s""s""e""r""t""S""e""l""e""c""t"" ""="" ""a""s""s""e""r""t""S""e""l""e""c""t""s""
""
"" "" "" "" ""d""e""f"" ""a""s""s""e""r""t""S""e""l""e""c""t""M""u""l""t""i""p""l""e""(""s""e""l""f"","" ""*""t""e""s""t""s"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""s""e""l""e""c""t""o""r"","" ""e""x""p""e""c""t""e""d""_""i""d""s"" ""i""n"" ""t""e""s""t""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""(""s""e""l""e""c""t""o""r"","" ""e""x""p""e""c""t""e""d""_""i""d""s"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""o""n""e""_""t""a""g""_""o""n""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""e""l""s"" ""="" ""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""t""i""t""l""e""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""e""l""s"")"","" ""1"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""e""l""s""[""0""]"".""n""a""m""e"","" ""'""t""i""t""l""e""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""e""l""s""[""0""]"".""c""o""n""t""e""n""t""s"","" ""[""u""'""T""h""e"" ""t""i""t""l""e""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""o""n""e""_""t""a""g""_""m""a""n""y""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""e""l""s"" ""="" ""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""d""i""v""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""e""l""s"")"","" ""3"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""d""i""v"" ""i""n"" ""e""l""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""d""i""v"".""n""a""m""e"","" ""'""d""i""v""'"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""t""a""g""_""i""n""_""t""a""g""_""o""n""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""e""l""s"" ""="" ""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""d""i""v"" ""d""i""v""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""'""d""i""v"" ""d""i""v""'"","" ""[""'""i""n""n""e""r""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""t""a""g""_""i""n""_""t""a""g""_""m""a""n""y""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""s""e""l""e""c""t""o""r"" ""i""n"" ""(""'""h""t""m""l"" ""d""i""v""'"","" ""'""h""t""m""l"" ""b""o""d""y"" ""d""i""v""'"","" ""'""b""o""d""y"" ""d""i""v""'"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""s""e""l""e""c""t""o""r"","" ""[""'""m""a""i""n""'"","" ""'""i""n""n""e""r""'"","" ""'""f""o""o""t""e""r""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""t""a""g""_""n""o""_""m""a""t""c""h""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""d""e""l""'"")"")"","" ""0"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""i""n""v""a""l""i""d""_""t""a""g""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""t""a""g""%""t""'"")"")"","" ""0"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""h""e""a""d""e""r""_""t""a""g""s""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""M""u""l""t""i""p""l""e""(""
"" "" "" "" "" "" "" "" "" "" "" "" ""(""'""h""1""'"","" ""[""'""h""e""a""d""e""r""1""'""]"")"",""
"" "" "" "" "" "" "" "" "" "" "" "" ""(""'""h""2""'"","" ""[""'""h""e""a""d""e""r""2""'"","" ""'""h""e""a""d""e""r""3""'""]"")"",""
"" "" "" "" "" "" "" "" "")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""c""l""a""s""s""_""o""n""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""s""e""l""e""c""t""o""r"" ""i""n"" ""(""'"".""o""n""e""p""'"","" ""'""p"".""o""n""e""p""'"","" ""'""h""t""m""l"" ""p"".""o""n""e""p""'"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s"" ""="" ""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""s""e""l""e""c""t""o""r"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""e""l""s"")"","" ""1"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""e""l""s""[""0""]"".""n""a""m""e"","" ""'""p""'"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""e""l""s""[""0""]""[""'""c""l""a""s""s""'""]"","" ""[""'""o""n""e""p""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""c""l""a""s""s""_""m""i""s""m""a""t""c""h""e""d""_""t""a""g""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""e""l""s"" ""="" ""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""d""i""v"".""o""n""e""p""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""e""l""s"")"","" ""0"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""o""n""e""_""i""d""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""s""e""l""e""c""t""o""r"" ""i""n"" ""(""'""d""i""v""#""i""n""n""e""r""'"","" ""'""#""i""n""n""e""r""'"","" ""'""d""i""v"" ""d""i""v""#""i""n""n""e""r""'"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""s""e""l""e""c""t""o""r"","" ""[""'""i""n""n""e""r""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""b""a""d""_""i""d""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""e""l""s"" ""="" ""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""#""d""o""e""s""n""o""t""e""x""i""s""t""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""e""l""s"")"","" ""0"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""i""t""e""m""s""_""i""n""_""i""d""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""e""l""s"" ""="" ""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""'""d""i""v""#""i""n""n""e""r"" ""p""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""e""l""s"")"","" ""3"")""
"" "" "" "" "" "" "" "" ""f""o""r"" ""e""l"" ""i""n"" ""e""l""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""e""l"".""n""a""m""e"","" ""'""p""'"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""e""l""s""[""1""]""[""'""c""l""a""s""s""'""]"","" ""[""'""o""n""e""p""'""]"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""F""a""l""s""e""(""e""l""s""[""0""]"".""h""a""s""_""k""e""y""(""'""c""l""a""s""s""'"")"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""a""_""b""u""n""c""h""_""o""f""_""e""m""p""t""y""s""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""s""e""l""e""c""t""o""r"" ""i""n"" ""(""'""d""i""v""#""m""a""i""n"" ""d""e""l""'"","" ""'""d""i""v""#""m""a""i""n"" ""d""i""v"".""o""o""p""s""'"","" ""'""d""i""v"" ""d""i""v""#""m""a""i""n""'"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""l""e""n""(""s""e""l""f"".""s""o""u""p"".""s""e""l""e""c""t""(""s""e""l""e""c""t""o""r"")"")"","" ""0"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""m""u""l""t""i""_""c""l""a""s""s""_""s""u""p""p""o""r""t""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""s""e""l""e""c""t""o""r"" ""i""n"" ""(""'"".""c""l""a""s""s""1""'"","" ""'""p"".""c""l""a""s""s""1""'"","" ""'"".""c""l""a""s""s""2""'"","" ""'""p"".""c""l""a""s""s""2""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" ""'"".""c""l""a""s""s""3""'"","" ""'""p"".""c""l""a""s""s""3""'"","" ""'""h""t""m""l"" ""p"".""c""l""a""s""s""2""'"","" ""'""d""i""v""#""i""n""n""e""r"" "".""c""l""a""s""s""2""'"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""s""e""l""e""c""t""o""r"","" ""[""'""p""m""u""l""t""i""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""m""u""l""t""i""_""c""l""a""s""s""_""s""e""l""e""c""t""i""o""n""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""f""o""r"" ""s""e""l""e""c""t""o""r"" ""i""n"" ""(""'"".""c""l""a""s""s""1"".""c""l""a""s""s""3""'"","" ""'"".""c""l""a""s""s""3"".""c""l""a""s""s""2""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'"".""c""l""a""s""s""1"".""c""l""a""s""s""2"".""c""l""a""s""s""3""'"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""s""e""l""e""c""t""o""r"","" ""[""'""p""m""u""l""t""i""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""c""h""i""l""d""_""s""e""l""e""c""t""o""r""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""'"".""s""1"" "">"" ""a""'"","" ""[""'""s""1""a""1""'"","" ""'""s""1""a""2""'""]"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""s""(""'"".""s""1"" "">"" ""a"" ""s""p""a""n""'"","" ""[""'""s""1""a""2""s""1""'""]"")""
""
"" "" "" "" ""d""e""f"" ""t""e""s""t""_""a""t""t""r""i""b""u""t""e""_""e""q""u""a""l""s""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""S""e""l""e""c""t""M""u""l""t""i""p""l""e""(""
"" "" "" "" "" "" "" "" "" "" "" "" ""(""'""p""[""c""l""a""s""s""=