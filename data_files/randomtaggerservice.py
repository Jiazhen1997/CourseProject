



from argparse import ArgumentParser
from cgi import FieldStorage

try:
    from json import dumps
except ImportError:
    
    from sys import path as sys_path
    from os.path import join as path_join
    from os.path import dirname
    sys_path.append(path_join(dirname(__file__), '../server/lib/ujson'))
    from ujson import dumps

from random import choice, randint
from sys import stderr
from urlparse import urlparse
try:
    from urlparse import parse_qs
except ImportError:
    
    from cgi import parse_qs
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler


ARGPARSER = ArgumentParser(description='An example HTTP tagging service, '
        'tagging Confuse-a-Cat **AND** Dead-parrot mentions!')
ARGPARSER.add_argument('-p', '--port', type=int, default=47111,
        help='port to run the HTTP service on (default: 47111)')


def _random_span(text):
    
    attempt = 1
    while True:
        start = randint(0, len(text))
        end = randint(start + 3, start + 25)

        
        if (
                
                end > len(text) or
                
                '\n' in text[start:end] or
                
                (text[start:end][-1] == ' ' or text[start:end][0] == ' ')
                ):
            
            if attempt >= 100:
                
                return None, None, None
            attempt += 1
            continue
        else:
            
            return start, end, text[start:end]

def _random_tagger(text):
    
    anns = {}
    if not text:
        
        return anns

    num_anns = randint(1, len(text) / 100)
    for ann_num in xrange(num_anns):
        ann_id = 'T%d' % ann_num
        
        _type = choice(('Confuse-a-Cat', 'Dead-parrot', ))
        start, end, span_text = _random_span(text)
        if start is None:
            
            continue
        anns[ann_id] = {
                'type': _type,
                'offsets': ((start, end), ),
                'texts': (span_text, ),
                }
    return anns

class RandomTaggerHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        field_storage = FieldStorage(
                headers=self.headers,
                environ={
                    'REQUEST_METHOD':'POST',
                    'CONTENT_TYPE':self.headers['Content-type'],
                    },
                fp=self.rfile)

        
        try:
            json_dic = _random_tagger(field_storage.value.decode('utf-8'))
        except KeyError:
            
            json_dic = {}

        
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()

        self.wfile.write(dumps(json_dic))
        print >> stderr, ('Generated %d random annotations' % len(json_dic))

    def log_message(self, format, *args):
        return 

def main(args):
    argp = ARGPARSER.parse_args(args[1:])

    server_class = HTTPServer
    httpd = server_class(('localhost', argp.port), RandomTaggerHandler)
    print >> stderr, 'Random tagger service started on port %s' % (argp.port)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print >> stderr, 'Random tagger service stopped'

if __name__ == '__main__':
    from sys import argv
    exit(main(argv))
