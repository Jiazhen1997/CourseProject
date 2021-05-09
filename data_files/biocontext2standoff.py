

import sys
import re
import os

options = None

DEFAULT_INPUT = 'entities-anatomy.csv'


BIOCONTEXT_ID_RE = re.compile(r'^([0-9]+|PMC[0-9]+\.[0-9]+\.[0-9])+$')

def argparser():
    import argparse
    
    ap=argparse.ArgumentParser(description='Convert BioContext data ' +
                               'into brat-flavored standoff.')
    ap.add_argument('-d', '--directory', default=None,
                    help='Output directory (default output to STDOUT)')
    ap.add_argument('-e', '--entitytype', default='Anatomical_entity',
                    help='Type to assign to annotations.')
    ap.add_argument('-f', '--file', default=DEFAULT_INPUT,
                    help='BioContext data (default "'"+"D"E"F"A"U"L"T"_"I"N"P"U"T"+"'"")""'"")""
"" "" "" "" ""a""p"".""a""d""d""_""a""r""g""u""m""e""n""t""(""'""-""n""'"","" ""'""-""-""n""o""-""n""o""r""m""'"","" ""d""e""f""a""u""l""t""=""F""a""l""s""e"","" ""a""c""t""i""o""n""=""'""s""t""o""r""e""_""t""r""u""e""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""h""e""l""p""=""'""D""o"" ""n""o""t"" ""o""u""t""p""u""t"" ""n""o""r""m""a""l""i""z""a""t""i""o""n"" ""a""n""n""o""t""a""t""i""o""n""s""'"")""
"" "" "" "" ""a""p"".""a""d""d""_""a""r""g""u""m""e""n""t""(""'""-""o""'"","" ""'""-""-""o""u""t""s""u""f""f""i""x""'"","" ""d""e""f""a""u""l""t""=""'""a""n""n""'"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""h""e""l""p""=""'""S""u""f""f""i""x"" ""t""o"" ""a""d""d"" ""t""o"" ""o""u""t""p""u""t"" ""f""i""l""e""s"" ""(""d""e""f""a""u""l""t"" Given a list of either document IDs in BioContext format or
    names of files containing one ID per line, return the combined set
    of IDs.