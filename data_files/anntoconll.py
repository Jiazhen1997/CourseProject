




from __future__ import with_statement

import sys
import re
import os

from collections import namedtuple
from os import path
from subprocess import Popen, PIPE
from cStringIO import StringIO
import io

sys.path.append(os.path.join(os.path.dirname(__file__), '../server/src'))
sys.path.append('.')
from sentencesplit import sentencebreaks_to_newlines

options = None

EMPTY_LINE_RE = re.compile(r'^\s*$')
CONLL_LINE_RE = re.compile(r'^\S+\t\d+\t\d+.')

class FormatError(Exception):
    pass

def argparser_internal():
    import argparse

    ap=argparse.ArgumentParser(description='Convert text and standoff ' +
                                           'annotations into CoNLL format.')
    ap.add_argument('-a', '--annsuffix', default="."a"n"n"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""h""e""l""p""=""'""S""t""a""n""d""o""f""f"" ""a""n""n""o""t""a""t""i""o""n"" ""f""i""l""e"" ""s""u""f""f""i""x"" ""(""d""e""f""a""u""l""t"" Return lines for one sentence from the CoNLL-formatted file.
    Sentences are delimited by empty lines.
    Given CoNLL-format lines, strip the label (first TAB-separated
    field) from each non-empty line. Return list of labels and list
    of lines without labels. Returned list of labels contains None
    for each empty line in the input.
    Given a list of labels and CoNLL-format lines, affix
    TAB-separated label to each non-empty line. Returns list of lines
    with attached labels.
    Convert plain text into CoNLL format.Parse textbound annotations in input, returning a list of
    Textbound.
    