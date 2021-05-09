



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

import json
import urllib
import urllib2
import base64




ARGPARSER = ArgumentParser(description='An example HTTP tagging service, '
				'tagging Confuse-a-Cat **AND** Dead-parrot mentions!')
ARGPARSER.add_argument('-p', '--port', type=int, default=56789,
				help='port to run the HTTP service on (default: 56789)')









def build_headers(email="","" ""p""a""s""s""w""o""r""d""=