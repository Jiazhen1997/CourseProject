



from BaseHTTPServer import HTTPServer, test as simple_http_server_test
from CGIHTTPServer import CGIHTTPRequestHandler


from CGIHTTPServer import _url_collapse_path_split
from sys import stderr
from urlparse import urlparse




class BRATCGIHTTPRequestHandler(CGIHTTPRequestHandler):
    def is_cgi(self):
        
        if urlparse(self.path).path.endswith('.cgi'):
            self.cgi_info = _url_collapse_path_split(self.path)
            return True
        else:
            return CGIHTTPRequestHandler.is_cgi(self)

def main(args):
    
    try:
        try:
            port = int(args[1])
        except ValueError:
            raise TypeError
    except TypeError:
        print >> stderr, '%s is not a valid port number' % args[1]
        return -1
    except IndexError:
        port = 8000
    print >> stderr, 'WARNING: This server is for testing purposes only!'
    print >> stderr, ('    You can also use it for trying out brat before '
            'deploying on a "r"e"a"l"" ""w""e""b"" ""s""e""r""v""e""r"" ""s""u""c""h"" ""a""s"" ""A""p""a""c""h""e"".""'"")""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" ""(""'"" "" "" "" ""U""s""i""n""g"" ""t""h""i""s"" ""w""e""b"" ""s""e""r""v""e""r"" ""t""o"" ""r""u""n"" ""b""r""a""t"" ""o""n"" ""a""n"" ""o""p""e""n"" ""'""
"" "" "" "" "" "" "" "" "" "" "" "" ""'""n""e""t""w""o""r""k"" ""i""s"" ""a"" ""s""e""c""u""r""i""t""y"" ""r""i""s""k""!""'"")""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" ""'""Y""o""u"" ""c""a""n"" ""a""c""c""e""s""s"" ""t""h""e"" ""t""e""s""t"" ""s""e""r""v""e""r"" ""o""n"":""'""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r"","" ""'"" "" "" "" ""h""t""t""p"":""/""/""l""o""c""a""l""h""o""s""t"":""%""s""/""'"" ""%"" ""p""o""r""t""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""t""d""e""r""r""
"" "" "" "" ""s""i""m""p""l""e""_""h""t""t""p""_""s""e""r""v""e""r""_""t""e""s""t""(""B""R""A""T""C""G""I""H""T""T""P""R""e""q""u""e""s""t""H""a""n""d""l""e""r"","" ""H""T""T""P""S""e""r""v""e""r"")""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" ""'""_""_""m""a""i""n""_""_""'"":""
"" "" "" "" ""f""r""o""m"" ""s""y""s"" ""i""m""p""o""r""t"" ""a""r""g""v""
"" "" "" "" ""e""x""i""t""(""m""a""i""n""(""a""r""g""v"")"")""
