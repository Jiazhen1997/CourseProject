import collections
import re
import sys
import warnings
from bs4.dammit import EntitySubstitution

DEFAULT_OUTPUT_ENCODING = "u"t"f"-"8""
""P""Y""3""K"" ""="" ""(""s""y""s"".""v""e""r""s""i""o""n""_""i""n""f""o""[""0""]"" "">"" ""2"")""
""
""w""h""i""t""e""s""p""a""c""e""_""r""e"" ""="" ""r""e"".""c""o""m""p""i""l""e""(Alias one attribute name to another for backward compatibilityA stand-in object for a character encoding specified in HTML.A generic stand-in for the value of a meta tag's 'charset' attribute.

    When Beautiful Soup parses the markup '<meta charset="u"t"f"8"">""'"","" ""t""h""e""
"" "" "" "" ""v""a""l""u""e"" ""o""f"" ""t""h""e"" ""'""c""h""a""r""s""e""t""'"" ""a""t""t""r""i""b""u""t""e"" ""w""i""l""l"" ""b""e"" ""o""n""e"" ""o""f"" ""t""h""e""s""e"" ""o""b""j""e""c""t""s"".""
"" "" "" "" A generic stand-in for the value of a meta tag's 'content' attribute.

    When Beautiful Soup parses the markup:
     <meta http-equiv="c"o"n"t"e"n"t"-"t"y"p"e"" ""c""o""n""t""e""n""t""=

    CHARSET_RE = re.compile("("("^"|";")"\"s"*"c"h"a"r"s"e"t"=")"("["^";"]"*")"","" ""r""e"".""M"")""
""
"" "" "" "" ""d""e""f"" ""_""_""n""e""w""_""_""(""c""l""s"","" ""o""r""i""g""i""n""a""l""_""v""a""l""u""e"")"":""
"" "" "" "" "" "" "" "" ""m""a""t""c""h"" ""="" ""c""l""s"".""C""H""A""R""S""E""T""_""R""E"".""s""e""a""r""c""h""(""o""r""i""g""i""n""a""l""_""v""a""l""u""e"")""
"" "" "" "" "" "" "" "" ""i""f"" ""m""a""t""c""h"" ""i""s"" ""N""o""n""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""N""o"" ""s""u""b""s""t""i""t""u""t""i""o""n"" ""n""e""c""e""s""s""a""r""y"".""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""u""n""i""c""o""d""e"".""_""_""n""e""w""_""_""(""u""n""i""c""o""d""e"","" ""o""r""i""g""i""n""a""l""_""v""a""l""u""e"")""
""
"" "" "" "" "" "" "" "" ""o""b""j"" ""="" ""u""n""i""c""o""d""e"".""_""_""n""e""w""_""_""(""c""l""s"","" ""o""r""i""g""i""n""a""l""_""v""a""l""u""e"")""
"" "" "" "" "" "" "" "" ""o""b""j"".""o""r""i""g""i""n""a""l""_""v""a""l""u""e"" ""="" ""o""r""i""g""i""n""a""l""_""v""a""l""u""e""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""o""b""j""
""
"" "" "" "" ""d""e""f"" ""e""n""c""o""d""e""(""s""e""l""f"","" ""e""n""c""o""d""i""n""g"")"":""
"" "" "" "" "" "" "" "" ""d""e""f"" ""r""e""w""r""i""t""e""(""m""a""t""c""h"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""m""a""t""c""h"".""g""r""o""u""p""(""1"")"" ""+"" ""e""n""c""o""d""i""n""g""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""C""H""A""R""S""E""T""_""R""E"".""s""u""b""(""r""e""w""r""i""t""e"","" ""s""e""l""f"".""o""r""i""g""i""n""a""l""_""v""a""l""u""e"")""
""
""
""c""l""a""s""s"" ""P""a""g""e""E""l""e""m""e""n""t""(""o""b""j""e""c""t"")"":""
"" "" "" "" 

    
    
    
    
    
    
    
    
    
    
    
    
    FORMATTERS = {
        "h"t"m"l"" "":"" ""E""n""t""i""t""y""S""u""b""s""t""i""t""u""t""i""o""n"".""s""u""b""s""t""i""t""u""t""e""_""h""t""m""l"",""
"" "" "" "" "" "" "" "" Format the given string using the given formatter.Sets up the initial relations between this element and
        other elements.Destructively rips this element out of the tree.Appends the given tag to the contents of this tag.Makes the given element the immediate predecessor of this one.

        The two elements will have the same parent, and the given element
        will be immediately before this one.
        Makes the given element the immediate successor of this one.

        The two elements will have the same parent, and the given element
        will be immediately after this one.
        Returns the first item that matches the given criteria and
        appears after this Tag in the document.Returns all items that match the given criteria and appear
        after this Tag in the document.Returns the closest sibling to this Tag that matches the
        given criteria and appears after this Tag in the document.Returns the siblings of this Tag that match the given
        criteria and appear after this Tag in the document.Returns the first item that matches the given criteria and
        appears before this Tag in the document.Returns all items that match the given criteria and appear
        before this Tag in the document.Returns the closest sibling to this Tag that matches the
        given criteria and appears before this Tag in the document.Returns the siblings of this Tag that match the given
        criteria and appear before this Tag in the document.Returns the closest parent of this Tag that matches the given
        criteria.Returns the parents of this Tag that match the given
        criteria.Force an attribute value into a string representation.

        A multi-valued attribute will be converted into a
        space-separated stirng.
        Create a function that performs a CSS selector operation.

        Takes an operator, attribute and optional value. Returns a
        function that will return True for elements that match that
        combination.
        Perform a CSS selection operation on the current element.Create a new NavigableString.

        When unpickling a NavigableString, this method is called with
        the string in DEFAULT_OUTPUT_ENCODING. That encoding needs to be
        passed in to the superclass's __new__ or the superclass won't know
        how to handle non-ASCII characters.
        text.string gives you text. This is for backwards
        compatibility for Navigable*String, but for CData* it lets you
        get the string without the CData wrapper.A NavigableString not subject to the normal formatting rules.

    The string will be passed into the formatter (to trigger side effects),
    but the return value will be ignored.
    CData strings are passed into the formatter.
        But the return value is ignored.Represents a found HTML tag with its attributes and contents.Is this tag an empty-element tag? (aka a self-closing tag)

        A tag that has contents is never an empty-element tag.

        A tag that has no contents may or may not be an empty-element
        tag. It depends on the builder used to create the tag. If the
        builder has a designated list of empty-element tags, then only
        a tag whose name shows up in that list is considered an
        empty-element tag.

        If the builder has no designated list of empty-element tags,
        then any tag with no contents is an empty-element tag.
        Convenience property to get the single string within this tag.

        :Return: If this tag has a single string child, return value
         is that string. If this tag has no children, or more than one
         child, return value is None. If this tag has one child tag,
         return value is the 'string' attribute of the child tag,
         recursively.
        Yield all child strings, possibly stripping them.
        Get all child strings, concatenated using the given separator.
        Recursively destroys the contents of this tree.
        Extract all children. If decompose is True, decompose instead.
        
        Find the index of a child by identity, not value. Avoids issues with
        tag.contents.index(element) getting the index of equal elements.
        Returns the value of the 'key' attribute for the tag, or
        the value given for 'default' if it doesn't have that
        attribute.tag[key] returns the value of the 'key' attribute for the tag,
        and throws an exception if it's not there.Setting tag[key] sets the value of the 'key' attribute for the
        tag.Calling a tag like a function is the same as calling its
        find_all() method. Eg. tag('a') returns a list of all the A tags
        found within this tag.Returns true iff this tag has the same name, the same attributes,
        and the same contents (recursively) as the given tag.Returns true iff this tag is not identical to the other tag,
        as defined in __eq__.Renders this tag as a string.Returns a Unicode representation of this tag and its contents.

        :param eventual_encoding: The tag is destined to be
           encoded into this encoding. This method is _not_
           responsible for performing that encoding. This information
           is passed in so that it can be substituted in if the
           document contains a <META> tag that mentions the document's
           encoding.
        Renders the contents of this tag as a Unicode string.

        :param eventual_encoding: The tag is destined to be
           encoded into this encoding. This method is _not_
           responsible for performing that encoding. This information
           is passed in so that it can be substituted in if the
           document contains a <META> tag that mentions the document's
           encoding.
        Renders the contents of this tag as a bytestring.Return only the first child of this Tag matching the given
        criteria.Extracts a list of Tag objects that match the given
        criteria.  You can specify the name of the Tag and any
        attributes you want the Tag to have.

        The value of a key-value pair in the 'attrs' map can be a
        string, a list of strings, a regular expression object, or a
        callable that takes a string and returns whether or not the
        string matches for some custom definition of 'matches'. The
        same is true of the tag name.Encapsulates a number of ways of matching a markup element (tag or
    text).A ResultSet is just a list that keeps track of the SoupStrainer
    that created it.