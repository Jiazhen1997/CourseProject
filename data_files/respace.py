




from __future__ import with_statement

import sys
import os
import re
import codecs


try:
    import xml.etree.ElementTree as ET
except ImportError: 
    import cElementTree as ET










INSERTED_ELEMENT_TAG = "n"2"t"-"s"p"c""
""
""I""N""P""U""T""_""E""N""C""O""D""I""N""G""=
    Returns the index of the given element in its parent element e.
    
    Eliminates multiple consequtive spaces and normalizes newlines
    (and other space) into regular space.
    
    Removes initial and terminal space from elements that either have
    surrounding space or belong to given set of elements to strip.
    
    Trims the beginning of the tail of elements where it is preceded
    by space.
    
    Performs space-removing normalizations.
    