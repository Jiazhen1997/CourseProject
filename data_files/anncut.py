





from __future__ import with_statement

import sys
import re

try:
    import argparse
except ImportError:
    from os.path import basename
    from sys import path as sys_path
    
    sys_path.append(join_path(basename(__file__), '../server/lib'))
    import argparse


class ArgumentError(Exception):
    def __init__(self, s):
        self.errstr = s

    def __str__(self):
        return 'Argument error: %s' % (self.errstr)

def argparser():
    ap=argparse.ArgumentParser(description="R"e"m"o"v"e" "p"o"r"t"i"o"n"s" "o"f" "t"e"x"t" "f"r"o"m" "a"n"n"o"t"a"t"e"d" "f"i"l"e"s"."")""
"" "" "" "" ""a""p"".""a""d""d""_""a""r""g""u""m""e""n""t""(