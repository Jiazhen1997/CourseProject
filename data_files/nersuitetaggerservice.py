



from argparse import ArgumentParser

from os.path import join as path_join
from os.path import dirname

try:
    from json import dumps
except ImportError:
    
    from sys import path as sys_path
    sys_path.append(path_join(dirname(__file__), '../server/lib/ujson'))
    from ujson import dumps

from subprocess import PIPE, Popen

from random import choice, randint
from sys import stderr
from urlparse import urlparse
try:
    from urlparse import parse_qs
except ImportError:
    
    from cgi import parse_qs
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import re


from sentencesplit import sentencebreaks_to_newlines


from BIOtoStandoff import BIO_lines_to_standoff


DOCUMENT_BOUNDARY = 'END-DOCUMENT'
NERSUITE_SCRIPT   = path_join(dirname(__file__), './nersuite_tag.sh')
NERSUITE_COMMAND  = [NERSUITE_SCRIPT, '-multidoc', DOCUMENT_BOUNDARY]

ARGPARSER = ArgumentParser(description='An example HTTP tagging service using NERsuite')
ARGPARSER.add_argument('-p', '--port', type=int, default=47111,
        help='port to run the HTTP service on (default: 47111)')



tagger_process = None

def run_tagger(cmd):
    
    global tagger_process
    try:
        tagger_process = Popen(cmd, stdin=PIPE, stdout=PIPE, bufsize=1)
    except Exception, e:
        print >> stderr, "E"r"r"o"r" "r"u"n"n"i"n"g" "'"%"s"'":"" ""%"" ""c""m""d"","" ""e""
"" "" "" "" "" "" "" "" ""r""a""i""s""e""
""
""d""e""f"" ""_""a""p""p""l""y""_""t""a""g""g""e""r""(""t""e""x""t"")"":""
"" "" "" "" ""g""l""o""b""a""l"" ""t""a""g""g""e""r""_""p""r""o""c""e""s""s"","" ""t""a""g""g""e""r""_""q""u""e""u""e""
""
"" "" "" "" ""#"" ""t""h""e"" ""t""a""g""g""e""r"" ""e""x""p""e""c""t""s"" ""a"" ""s""e""n""t""e""n""c""e"" ""p""e""r"" ""l""i""n""e"","" ""s""o"" ""d""o"" ""b""a""s""i""c"" ""s""p""l""i""t""t""i""n""g""
"" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" ""s""p""l""i""t""t""e""x""t"" ""="" ""s""e""n""t""e""n""c""e""b""r""e""a""k""s""_""t""o""_""n""e""w""l""i""n""e""s""(""t""e""x""t"")""
"" "" "" "" ""e""x""c""e""p""t"":""
"" "" "" "" "" "" "" "" ""#"" ""i""f"" ""a""n""y""t""h""i""n""g"" ""g""o""e""s"" ""w""r""o""n""g"","" ""j""u""s""t"" ""g""o"" ""w""i""t""h"" ""t""h""e""
"" "" "" "" "" "" "" "" ""#"" ""o""r""i""g""i""n""a""l"" ""t""e""x""t"" ""i""n""s""t""e""a""d""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" 