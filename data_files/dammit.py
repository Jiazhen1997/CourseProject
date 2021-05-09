


import codecs
from htmlentitydefs import codepoint2name
import re
import logging


chardet_type = None
try:
    
    
    import cchardet
    def chardet_dammit(s):
        return cchardet.detect(s)['encoding']
except ImportError:
    try:
        
        
        
        import chardet
        def chardet_dammit(s):
            return chardet.detect(s)['encoding']
        
        
    except ImportError:
        
        def chardet_dammit(s):
            return None


try:
    import iconv_codec
except ImportError:
    pass

xml_encoding_re = re.compile(
    '^<\?.*encoding=[\'"](.*?)[\'"].*\?>'.encode(), re.I)
html_meta_re = re.compile(
    '<\s*meta[^>]+charset\s*=\s*["\"'"]"?"("["^">"]"*"?")"[" "/";"\"'"">""]""'"".""e""n""c""o""d""e""("")"","" ""r""e"".""I"")""
""
""c""l""a""s""s"" ""E""n""t""i""t""y""S""u""b""s""t""i""t""u""t""i""o""n""(""o""b""j""e""c""t"")"":""
""
"" "" "" "" 

    def _populate_class_variables():
        lookup = {}
        reverse_lookup = {}
        characters_for_re = []
        for codepoint, name in list(codepoint2name.items()):
            character = unichr(codepoint)
            if codepoint != 34:
                
                
                
                characters_for_re.append(character)
                lookup[character] = name
            
            reverse_lookup[name] = character
        re_definition = "["%"s"]"" ""%"" Used with a regular expression to substitute the
        appropriate XML entity for an XML special character.Make a value into a quoted XML attribute, possibly escaping it.

         Most strings will be quoted using double quotes.

          Bob's Bar -> "B"o"b"'"s" "B"a"r""
""
"" "" "" "" "" "" "" "" "" ""I""f"" ""a"" ""s""t""r""i""n""g"" ""c""o""n""t""a""i""n""s"" ""d""o""u""b""l""e"" ""q""u""o""t""e""s"","" ""i""t"" ""w""i""l""l"" ""b""e"" ""q""u""o""t""e""d"" ""u""s""i""n""g""
"" "" "" "" "" "" "" "" "" ""s""i""n""g""l""e"" ""q""u""o""t""e""s"".""
""
"" "" "" "" "" "" "" "" "" "" ""W""e""l""c""o""m""e"" ""t""o"" 
        quote_with = '"'
        if '"' in value:
            if "'"" ""i""n"" ""v""a""l""u""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""T""h""e"" ""s""t""r""i""n""g"" ""c""o""n""t""a""i""n""s"" ""b""o""t""h"" ""s""i""n""g""l""e"" ""a""n""d"" ""d""o""u""b""l""e""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""q""u""o""t""e""s""."" "" ""T""u""r""n"" ""t""h""e"" ""d""o""u""b""l""e"" ""q""u""o""t""e""s"" ""i""n""t""o""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""e""n""t""i""t""i""e""s""."" ""W""e"" ""q""u""o""t""e"" ""t""h""e"" ""d""o""u""b""l""e"" ""q""u""o""t""e""s"" ""r""a""t""h""e""r"" ""t""h""a""n""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""t""h""e"" ""s""i""n""g""l""e"" ""q""u""o""t""e""s"" ""b""e""c""a""u""s""e"" ""t""h""e"" ""e""n""t""i""t""y"" ""n""a""m""e"" ""i""s""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" Substitute XML entities for special XML characters.

        :param value: A string to be substituted. The less-than sign will
          become &lt;, the greater-than sign will become &gt;, and any
          ampersands that are not part of an entity defition will
          become &amp;.

        :param make_quoted_attribute: If True, then the string will be
         quoted, as befits an attribute value.
        Replace certain Unicode characters with named HTML entities.

        This differs from data.encode(encoding, 'xmlcharrefreplace')
        in that the goal is to make the result more readable (to those
        with ASCII displays) rather than to recover from
        errors. There's absolutely nothing wrong with a UTF-8 string
        containg a LATIN SMALL LETTER E WITH ACUTE, but replacing that
        character with "&"e"a"c"u"t"e";"" ""w""i""l""l"" ""m""a""k""e"" ""i""t"" ""m""o""r""e"" ""r""e""a""d""a""b""l""e"" ""t""o"" ""s""o""m""e""
"" "" "" "" "" "" "" "" ""p""e""o""p""l""e"".""
"" "" "" "" "" "" "" "" A class for detecting the encoding of a *ML document and
    converting it to a Unicode string. If the source encoding is
    windows-1252, can replace MS smart quotes with their HTML or XML
    equivalents.Changes a MS smart quote character to an XML or HTML
        entity, or an ASCII character.Given a document, tries to detect its XML encoding.Fix characters from one encoding embedded in some other encoding.

        Currently the only situation supported is Windows-1252 (or its
        subset ISO-8859-1), embedded in UTF-8.

        The input must be a bytestring. If you've already converted
        the document to Unicode, you're too late.

        The output is a bytestring in which `embedded_encoding`
        characters have been converted to their `main_encoding`
        equivalents.
        