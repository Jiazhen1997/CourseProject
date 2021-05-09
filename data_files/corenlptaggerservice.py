



from argparse import ArgumentParser
from cgi import FieldStorage
from os.path import dirname, join as path_join

from corenlp import CoreNLPTagger

try:
    from json import dumps
except ImportError:
    
    from sys import path as sys_path
    sys_path.append(path_join(dirname(__file__), '../../server/lib/ujson'))
    from ujson import dumps

from sys import stderr
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


ARGPARSER = ArgumentParser(description='XXX')
ARGPARSER.add_argument('-p', '--port', type=int, default=47111,
        help='port to run the HTTP service on (default: 47111)')
TAGGER = None

CORENLP_PATH = path_join(dirname(__file__), 'stanford-corenlp-2012-04-09')



class CoreNLPTaggerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print >> stderr, 'Received request'
        field_storage = FieldStorage(
                headers=self.headers,
                environ={
                    'REQUEST_METHOD':'POST',
                    'CONTENT_TYPE':self.headers['Content-Type'],
                    },
                fp=self.rfile)

        global TAGGER
        json_dic = TAGGER.tag(field_storage.value)

        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()

        self.wfile.write(dumps(json_dic))
        print >> stderr, ('Generated %d annotations' % len(json_dic))

    def log_message(self, format, *args):
        return 

def main(args):
    argp = ARGPARSER.parse_args(args[1:])

    print >> stderr, "W"A"R"N"I"N"G":" "D"o"n"'"t" "u"s"e" "t"h"i"s" "i"n" "a" "p"r"o"d"u"c"t"i"o"n" "e"n"v"i"r"o"n"m"e"n"t"!""
""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" ""'""S""t""a""r""t""i""n""g"" ""C""o""r""e""N""L""P"" ""p""r""o""c""e""s""s"" ""(""t""h""i""s"" ""t""a""k""e""s"" ""a"" ""w""h""i""l""e"")"".""."".""'"",""
"" "" "" "" ""g""l""o""b""a""l"" ""T""A""G""G""E""R""
"" "" "" "" ""T""A""G""G""E""R"" ""="" ""C""o""r""e""N""L""P""T""a""g""g""e""r""(""C""O""R""E""N""L""P""_""P""A""T""H"")""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" ""'""D""o""n""e""!""'""
""
"" "" "" "" ""s""e""r""v""e""r""_""c""l""a""s""s"" ""="" ""H""T""T""P""S""e""r""v""e""r""
"" "" "" "" ""h""t""t""p""d"" ""="" ""s""e""r""v""e""r""_""c""l""a""s""s""(""(""'""l""o""c""a""l""h""o""s""t""'"","" ""a""r""g""p"".""p""o""r""t"")"","" ""C""o""r""e""N""L""P""T""a""g""g""e""r""H""a""n""d""l""e""r"")""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" ""'""C""o""r""e""N""L""P"" ""t""a""g""g""e""r"" ""s""e""r""v""i""c""e"" ""s""t""a""r""t""e""d""'""
"" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" ""h""t""t""p""d"".""s""e""r""v""e""_""f""o""r""e""v""e""r""("")""
"" "" "" "" ""e""x""c""e""p""t"" ""K""e""y""b""o""a""r""d""I""n""t""e""r""r""u""p""t"":""
"" "" "" "" "" "" "" "" ""p""a""s""s""
"" "" "" "" ""h""t""t""p""d"".""s""e""r""v""e""r""_""c""l""o""s""e""("")""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" ""'""C""o""r""e""N""L""P"" ""t""a""g""g""e""r"" ""s""e""r""v""i""c""e"" ""s""t""o""p""p""e""d""'""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" ""'""_""_""m""a""i""n""_""_""'"":""
"" "" "" "" ""f""r""o""m"" ""s""y""s"" ""i""m""p""o""r""t"" ""a""r""g""v""
"" "" "" "" ""e""x""i""t""(""m""a""i""n""(""a""r""g""v"")"")""
