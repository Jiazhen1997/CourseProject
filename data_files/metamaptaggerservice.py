



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


from MetaMaptoStandoff import MetaMap_lines_to_standoff


METAMAP_SCRIPT   = path_join(dirname(__file__), './metamap_tag.sh')
METAMAP_COMMAND  = [METAMAP_SCRIPT]

ARGPARSER = ArgumentParser(description='An example HTTP tagging service using MetaMap')
ARGPARSER.add_argument('-p', '--port', type=int, default=47111,
        help='port to run the HTTP service on (default: 47111)')


def run_tagger(cmd):
    
    try:
        tagger_process = Popen(cmd, stdin=PIPE, stdout=PIPE, bufsize=1)
        return tagger_process
    except Exception, e:
        print >> stderr, "E"r"r"o"r" "r"u"n"n"i"n"g" "'"%"s"'":"" ""%"" ""c""m""d"","" ""e""
"" "" "" "" "" "" "" "" ""r""a""i""s""e"" "" "" "" ""
""
""d""e""f"" ""_""a""p""p""l""y""_""t""a""g""g""e""r""_""t""o""_""s""e""n""t""e""n""c""e""(""t""e""x""t"")"":""
"" "" "" "" ""#"" ""c""a""n"" ""a""f""f""o""r""d"" ""t""o"" ""r""e""s""t""a""r""t"" ""t""h""i""s"" ""o""n"" ""e""a""c""h"" ""i""n""v""o""c""a""t""i""o""n""
"" "" "" "" ""t""a""g""g""e""r""_""p""r""o""c""e""s""s"" ""="" ""r""u""n""_""t""a""g""g""e""r""(""M""E""T""A""M""A""P""_""C""O""M""M""A""N""D"")""
""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""t""a""g""g""e""r""_""p""r""o""c""e""s""s"".""s""t""d""i""n"","" ""t""e""x""t""
"" "" "" "" ""t""a""g""g""e""r""_""p""r""o""c""e""s""s"".""s""t""d""i""n"".""c""l""o""s""e""("")""
"" "" "" "" ""t""a""g""g""e""r""_""p""r""o""c""e""s""s"".""w""a""i""t""("")""
""
"" "" "" "" ""r""e""s""p""o""n""s""e""_""l""i""n""e""s"" ""="" ""[""]""
""
"" "" "" "" ""f""o""r"" ""l"" ""i""n"" ""t""a""g""g""e""r""_""p""r""o""c""e""s""s"".""s""t""d""o""u""t"":""
"" "" "" "" "" "" "" "" ""l"" ""="" ""l"".""r""s""t""r""i""p""(""'""\""n""'"")""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e""_""l""i""n""e""s"".""a""p""p""e""n""d""(""l"")""
"" "" "" "" "" "" "" "" ""
"" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" ""t""a""g""g""e""d""_""e""n""t""i""t""i""e""s"" ""="" ""M""e""t""a""M""a""p""_""l""i""n""e""s""_""t""o""_""s""t""a""n""d""o""f""f""(""r""e""s""p""o""n""s""e""_""l""i""n""e""s"","" ""t""e""x""t"")""
"" "" "" "" ""e""x""c""e""p""t"":""
"" "" "" "" "" "" "" "" ""#"" ""i""f"" ""a""n""y""t""h""i""n""g"" ""g""o""e""s"" ""w""r""o""n""g"","" ""b""a""i""l"" ""o""u""t""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" 