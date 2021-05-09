








import sys
import os

from posixpath import normpath
from urllib import unquote

from cgi import FieldStorage
from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
from SocketServer import ForkingMixIn
import socket


sys.path.append(os.path.join(os.path.dirname(__file__), 'server/src'))
from server import serve


import annlog
import annotation
import annotator
import auth
import common
import delete
import dispatch
import docimport
import document
import download
import filelock
import gtbtokenize
import jsonwrap
import message
import normdb
import norm
import predict
import projectconfig
import realmessage
import sdistance
import search
import server
import session
import simstringdb
import sosmessage
import ssplit
import sspostproc
import stats
import svg
import tag
import tokenise
import undo
import verify_annotations

_VERBOSE_HANDLER = False
_DEFAULT_SERVER_ADDR = ''
_DEFAULT_SERVER_PORT = 8001

_PERMISSIONS = 

class PermissionParseError(Exception):
    def __init__(self, linenum, line, message=None):
        self.linenum = linenum
        self.line = line
        self.message = ' (%s)' % message if message is not None else ''
    
    def __str__(self):
        return 'line %d%s: %s' % (self.linenum, self.message, self.line)

class PathPattern(object):
    def __init__(self, path):
        self.path = path
        self.plen = len(path)

    def match(self, s):
        
        return s[:self.plen] == self.path and (self.path[-1] == '/' or
                                               s[self.plen:] == '' or 
                                               s[self.plen] == '/')

class ExtensionPattern(object):
    def __init__(self, ext):
        self.ext = ext

    def match(self, s):
        return os.path.splitext(s)[1] == self.ext

class PathPermissions(object):
    

    def __init__(self, default_allow=False):
        self._entries = []
        self.default_allow = default_allow

    def allow(self, path):
        
        for pattern, allow in self._entries:
            if pattern.match(path):
                return allow
        return self.default_allow
    
    def parse(self, lines):
        
        
        
        

        for ln, l in enumerate(lines):            
            i = l.find('#')
            if i != -1:
                l = l[:i]
            l = l.strip()

            if not l:
                continue

            i = l.find(':')
            if i == -1:
                raise PermissionParseError(ln, lines[ln], 'missing colon')

            directive = l[:i].strip().lower()
            pattern = l[i+1:].strip()

            if directive == 'allow':
                allow = True
            elif directive == 'disallow':
                allow = False
            else:
                raise PermissionParseError(ln, lines[ln], 'unrecognized directive')
            
            if pattern.startswith('/'):
                patt = PathPattern(pattern)
            elif pattern.startswith('*.'):
                patt = ExtensionPattern(pattern[1:])
            else:
                raise PermissionParseError(ln, lines[ln], 'unrecognized pattern')

            self._entries.append((patt, allow))

        return self

class BratHTTPRequestHandler(SimpleHTTPRequestHandler):
    

    permissions = PathPermissions().parse(_PERMISSIONS.split('\n'))

    def log_request(self, code='-', size='-'):
        if _VERBOSE_HANDLER:
            SimpleHTTPRequestHandler.log_request(self, code, size)
        else:
            
            pass

    def is_brat(self):
        
        path = self.path
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]

        if path == '/ajax.cgi':
            return True
        else:
            return False    

    def run_brat_direct(self):
        

        remote_addr = self.client_address[0]
        remote_host = self.address_string()
        cookie_data = ', '.join(filter(None, self.headers.getheaders('cookie')))

        query_string = ''
        i = self.path.find('?')
        if i != -1:
            query_string = self.path[i+1:]
            
        saved = sys.stdin, sys.stdout, sys.stderr
        sys.stdin, sys.stdout = self.rfile, self.wfile

        
        env = {}
        env['REQUEST_METHOD'] = self.command
        content_length = self.headers.getheader('content-length')
        if content_length:
            env['CONTENT_LENGTH'] = content_length
        if query_string:
            env['QUERY_STRING'] = query_string
        os.environ.update(env)
        params = FieldStorage()

        
        cookie_hdrs, response_data = serve(params, remote_addr, remote_host,
                                           cookie_data)

        sys.stdin, sys.stdout, sys.stderr = saved

        
        if cookie_hdrs is not None:
            response_hdrs = [hdr for hdr in cookie_hdrs]
        else:
            response_hdrs = []
        response_hdrs.extend(response_data[0])

        self.send_response(200)
        self.wfile.write('\n'.join('%s: %s' % (k, v) for k, v in response_hdrs))
        self.wfile.write('\n')
        self.wfile.write('\n')
        
        if isinstance(response_data[1], unicode):
            self.wfile.write(response_data[1].encode('utf-8'))
        else:
            self.wfile.write(response_data[1])
        return 0

    def allow_path(self):
        

        
        path = self.path
        path = path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = unquote(path)
        path = normpath(path)
        parts = path.split('/')
        parts = filter(None, parts)
        if '..' in parts:
            return False
        path = '/'+'/'.join(parts)

        return self.permissions.allow(path)

    def list_directory(self, path):
        
        
        self.send_error(403)

    def do_POST(self):
        

        if self.is_brat():
            self.run_brat_direct()
        else:
            self.send_error(501, "C"a"n" "o"n"l"y" "P"O"S"T" "t"o" "b"r"a"t"")""
""
"" "" "" "" ""d""e""f"" ""d""o""_""G""E""T""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" 
        if not self.allow_path():
            self.send_error(403)
        elif self.is_brat():
            self.run_brat_direct()
        else:
            SimpleHTTPRequestHandler.do_GET(self)

    def do_HEAD(self):
        
        if not self.allow_path():
            self.send_error(403)
        else:
            SimpleHTTPRequestHandler.do_HEAD(self)
       
class BratServer(ForkingMixIn, HTTPServer):
    def __init__(self, server_address):
        HTTPServer.__init__(self, server_address, BratHTTPRequestHandler)

def main(argv):
    
    try:
        if os.getuid() == 0:
            print >> sys.stderr, 
    except AttributeError:
        
        print >> sys.stderr, 

    if len(argv) > 1:
        try:
            port = int(argv[1])
        except ValueError:
            print >> sys.stderr, "F"a"i"l"e"d" "t"o" "p"a"r"s"e"","" ""a""r""g""v""[""1""]"","" 