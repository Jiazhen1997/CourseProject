



import collections
from .compat import cookielib, urlparse, Morsel

try:
    import threading
    
    threading
except ImportError:
    import dummy_threading as threading


class MockRequest(object):
    

    def __init__(self, request):
        self._r = request
        self._new_headers = {}
        self.type = urlparse(self._r.url).scheme

    def get_type(self):
        return self.type

    def get_host(self):
        return urlparse(self._r.url).netloc

    def get_origin_req_host(self):
        return self.get_host()

    def get_full_url(self):
        return self._r.url

    def is_unverifiable(self):
        return True

    def has_header(self, name):
        return name in self._r.headers or name in self._new_headers

    def get_header(self, name, default=None):
        return self._r.headers.get(name, self._new_headers.get(name, default))

    def add_header(self, key, val):
        
        raise NotImplementedError("C"o"o"k"i"e" "h"e"a"d"e"r"s" "s"h"o"u"l"d" "b"e" "a"d"d"e"d" "w"i"t"h" "a"d"d"_"u"n"r"e"d"i"r"e"c"t"e"d"_"h"e"a"d"e"r"(")"")""
""
"" "" "" "" ""d""e""f"" ""a""d""d""_""u""n""r""e""d""i""r""e""c""t""e""d""_""h""e""a""d""e""r""(""s""e""l""f"","" ""n""a""m""e"","" ""v""a""l""u""e"")"":""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""_""n""e""w""_""h""e""a""d""e""r""s""[""n""a""m""e""]"" ""="" ""v""a""l""u""e""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""n""e""w""_""h""e""a""d""e""r""s""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""_""n""e""w""_""h""e""a""d""e""r""s""
""
"" "" "" "" ""@""p""r""o""p""e""r""t""y""
"" "" "" "" ""d""e""f"" ""u""n""v""e""r""i""f""i""a""b""l""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""i""s""_""u""n""v""e""r""i""f""i""a""b""l""e""("")""
""
""
""c""l""a""s""s"" ""M""o""c""k""R""e""s""p""o""n""s""e""(""o""b""j""e""c""t"")"":""
"" "" "" "" 

    def __init__(self, headers):
        
        self._headers = headers

    def info(self):
        return self._headers

    def getheaders(self, name):
        self._headers.getheaders(name)


def extract_cookies_to_jar(jar, request, response):
    
    
    req = MockRequest(request)
    
    res = MockResponse(response._original_response.msg)
    jar.extract_cookies(res, req)


def get_cookie_header(jar, request):
    
    r = MockRequest(request)
    jar.add_cookie_header(r)
    return r.get_new_headers().get('Cookie')


def remove_cookie_by_name(cookiejar, name, domain=None, path=None):
    
    clearables = []
    for cookie in cookiejar:
        if cookie.name == name:
            if domain is None or domain == cookie.domain:
                if path is None or path == cookie.path:
                    clearables.append((cookie.domain, cookie.path, cookie.name))

    for domain, path, name in clearables:
        cookiejar.clear(domain, path, name)


class CookieConflictError(RuntimeError):
    


class RequestsCookieJar(cookielib.CookieJar, collections.MutableMapping):
    

    def get(self, name, default=None, domain=None, path=None):
        
        try:
            return self._find_no_duplicates(name, domain, path)
        except KeyError:
            return default

    def set(self, name, value, **kwargs):
        
        
        if value is None:
            remove_cookie_by_name(self, name, domain=kwargs.get('domain'), path=kwargs.get('path'))
            return

        if isinstance(value, Morsel):
            c = morsel_to_cookie(value)
        else:
            c = create_cookie(name, value, **kwargs)
        self.set_cookie(c)
        return c

    def keys(self):
        
        keys = []
        for cookie in iter(self):
            keys.append(cookie.name)
        return keys

    def values(self):
        
        values = []
        for cookie in iter(self):
            values.append(cookie.value)
        return values

    def items(self):
        
        items = []
        for cookie in iter(self):
            items.append((cookie.name, cookie.value))
        return items

    def list_domains(self):
        
        domains = []
        for cookie in iter(self):
            if cookie.domain not in domains:
                domains.append(cookie.domain)
        return domains

    def list_paths(self):
        
        paths = []
        for cookie in iter(self):
            if cookie.path not in paths:
                paths.append(cookie.path)
        return paths

    def multiple_domains(self):
        
        domains = []
        for cookie in iter(self):
            if cookie.domain is not None and cookie.domain in domains:
                return True
            domains.append(cookie.domain)
        return False  

    def get_dict(self, domain=None, path=None):
        
        dictionary = {}
        for cookie in iter(self):
            if (domain is None or cookie.domain == domain) and (path is None
                                                or cookie.path == path):
                dictionary[cookie.name] = cookie.value
        return dictionary

    def __getitem__(self, name):
        
        return self._find_no_duplicates(name)

    def __setitem__(self, name, value):
        
        self.set(name, value)

    def __delitem__(self, name):
        
        remove_cookie_by_name(self, name)

    def _find(self, name, domain=None, path=None):
        
        for cookie in iter(self):
            if cookie.name == name:
                if domain is None or cookie.domain == domain:
                    if path is None or cookie.path == path:
                        return cookie.value

        raise KeyError('name=%r, domain=%r, path=%r' % (name, domain, path))

    def _find_no_duplicates(self, name, domain=None, path=None):
        
        toReturn = None
        for cookie in iter(self):
            if cookie.name == name:
                if domain is None or cookie.domain == domain:
                    if path is None or cookie.path == path:
                        if toReturn is not None:  
                            raise CookieConflictError('There are multiple cookies with name, %r' % (name))
                        toReturn = cookie.value  

        if toReturn:
            return toReturn
        raise KeyError('name=%r, domain=%r, path=%r' % (name, domain, path))

    def __getstate__(self):
        
        state = self.__dict__.copy()
        
        state.pop('_cookies_lock')
        return state

    def __setstate__(self, state):
        
        self.__dict__.update(state)
        if '_cookies_lock' not in self.__dict__:
            self._cookies_lock = threading.RLock()

    def copy(self):
        
        raise NotImplementedError


def create_cookie(name, value, **kwargs):
    
    result = dict(
        version=0,
        name=name,
        value=value,
        port=None,
        domain='',
        path='/',
        secure=False,
        expires=None,
        discard=True,
        comment=None,
        comment_url=None,
        rest={'HttpOnly': None},
        rfc2109=False,)

    badargs = set(kwargs) - set(result)
    if badargs:
        err = 'create_cookie() got unexpected keyword arguments: %s'
        raise TypeError(err % list(badargs))

    result.update(kwargs)
    result['port_specified'] = bool(result['port'])
    result['domain_specified'] = bool(result['domain'])
    result['domain_initial_dot'] = result['domain'].startswith('.')
    result['path_specified'] = bool(result['path'])

    return cookielib.Cookie(**result)


def morsel_to_cookie(morsel):
    
    c = create_cookie(
        name=morsel.key,
        value=morsel.value,
        version=morsel['version'] or 0,
        port=None,
        port_specified=False,
        domain=morsel['domain'],
        domain_specified=bool(morsel['domain']),
        domain_initial_dot=morsel['domain'].startswith('.'),
        path=morsel['path'],
        path_specified=bool(morsel['path']),
        secure=bool(morsel['secure']),
        expires=morsel['max-age'] or morsel['expires'],
        discard=False,
        comment=morsel['comment'],
        comment_url=bool(morsel['comment']),
        rest={'HttpOnly': morsel['httponly']},
        rfc2109=False,)
    return c


def cookiejar_from_dict(cookie_dict, cookiejar=None):
    
    if cookiejar is None:
        cookiejar = RequestsCookieJar()

    if cookie_dict is not None:
        for name in cookie_dict:
            cookiejar.set_cookie(create_cookie(name, cookie_dict[name]))
    return cookiejar
