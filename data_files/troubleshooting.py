



from httplib import HTTPConnection, HTTPSConnection
from httplib import FORBIDDEN, MOVED_PERMANENTLY, NOT_FOUND, OK, TEMPORARY_REDIRECT
from sys import stderr
from urlparse import urlparse


CONNECTION_BY_SCHEME = {
        'http': HTTPConnection,
        'https': HTTPSConnection,
        }



def _request_wrap(conn, method, url, body=None,
        headers=None):
    depth = 0
    curr_conn = conn
    curr_url = url
    while depth < 100: 
        curr_conn.request(method, curr_url, body,
                headers=headers if headers is not None else {})
        res = curr_conn.getresponse()
        if res.status not in (MOVED_PERMANENTLY, TEMPORARY_REDIRECT, ):
            return res
        res.read() 
        res_headers = dict(res.getheaders())
        url_soup = urlparse(res_headers['location'])
        
        
        try:
            curr_conn = CONNECTION_BY_SCHEME[url_soup.scheme](url_soup.netloc)
        except KeyError:
            assert False, 'redirected to unknown scheme, dying'
        curr_url = url_soup.path
        depth += 1
    assert False, 'redirects and moves lead us astray, dying'

def main(args):
    
    if len(args) != 2:
        print >> stderr, 'Usage: %s url_to_brat_installation' % (args[0], )
        return -1
    brat_url = args[1]
    url_soup = urlparse(brat_url)

    if url_soup.scheme:
        try:
            Connection = CONNECTION_BY_SCHEME[url_soup.scheme.split(':')[0]]
        except KeyError:
            print >> stderr, ('ERROR: Unknown url scheme %s, try http or '
                    'https') % url_soup.scheme
            return -1
    else:
        
        path_soup = url_soup.path.split('/')
        assumed_netloc = path_soup[0]
        assumed_path = '/' + '/'.join(path_soup[1:])
        print >> stderr, ('WARNING: No url scheme given, assuming scheme: '
                '"http"," "n"e"t"l"o"c":" ""%""s