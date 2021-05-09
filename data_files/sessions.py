


import os

from .compat import cookielib
from .cookies import cookiejar_from_dict
from .models import Request
from .hooks import dispatch_hook, default_hooks
from .utils import from_key_val_list, default_headers
from .exceptions import TooManyRedirects, InvalidSchema

from .compat import urlparse, urljoin
from .adapters import HTTPAdapter

from .utils import requote_uri, get_environ_proxies, get_netrc_auth

from .status_codes import codes
REDIRECT_STATI = (codes.moved, codes.found, codes.other, codes.temporary_moved)
DEFAULT_REDIRECT_LIMIT = 30


def merge_kwargs(local_kwarg, default_kwarg):
    

    if default_kwarg is None:
        return local_kwarg

    if isinstance(local_kwarg, str):
        return local_kwarg

    if local_kwarg is None:
        return default_kwarg

    
    if not hasattr(default_kwarg, 'items'):
        return local_kwarg

    default_kwarg = from_key_val_list(default_kwarg)
    local_kwarg = from_key_val_list(local_kwarg)

    
    kwargs = default_kwarg.copy()
    kwargs.update(local_kwarg)

    
    for (k, v) in local_kwarg.items():
        if v is None:
            del kwargs[k]

    return kwargs


class SessionRedirectMixin(object):

    def resolve_redirects(self, resp, req, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        

        i = 0

        
        while (('location' in resp.headers and resp.status_code in REDIRECT_STATI)):

            resp.content  

            if i >= self.max_redirects:
                raise TooManyRedirects('Exceeded %s redirects.' % self.max_redirects)

            
            resp.close()

            url = resp.headers['location']
            method = req.method

            
            if url.startswith('//'):
                parsed_rurl = urlparse(resp.url)
                url = '%s:%s' % (parsed_rurl.scheme, url)

            
            
            if not urlparse(url).netloc:
                
                url = urljoin(resp.url, requote_uri(url))

            
            if resp.status_code is codes.see_other:
                method = 'GET'

            
            if resp.status_code in (codes.moved, codes.found) and req.method == 'POST':
                method = 'GET'

            if (resp.status_code == 303) and req.method != 'HEAD':
                method = 'GET'

            
            headers = req.headers
            try:
                del headers['Cookie']
            except KeyError:
                pass

            resp = self.request(
                    url=url,
                    method=method,
                    headers=headers,
                    params=req.params,
                    auth=req.auth,
                    cookies=req.cookies,
                    allow_redirects=False,
                    stream=stream,
                    timeout=timeout,
                    verify=verify,
                    cert=cert,
                    proxies=proxies
                )

            i += 1
            yield resp


class Session(SessionRedirectMixin):
    

    def __init__(self):

        
        
        
        self.headers = default_headers()

        
        
        self.auth = None

        
        
        
        self.proxies = {}

        
        self.hooks = default_hooks()

        
        
        
        self.params = {}

        
        self.stream = False

        
        self.verify = True

        
        self.cert = None

        
        self.max_redirects = DEFAULT_REDIRECT_LIMIT

        
        self.trust_env = True

        
        self.cookies = cookiejar_from_dict({})

        
        self.adapters = {}
        self.mount('http://', HTTPAdapter())
        self.mount('https://', HTTPAdapter())

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def request(self, method, url,
        params=None,
        data=None,
        headers=None,
        cookies=None,
        files=None,
        auth=None,
        timeout=None,
        allow_redirects=True,
        proxies=None,
        hooks=None,
        stream=None,
        verify=None,
        cert=None):

        cookies = cookies or {}
        proxies = proxies or {}

        
        if not isinstance(cookies, cookielib.CookieJar):
            cookies = cookiejar_from_dict(cookies)

        
        for cookie in self.cookies:
            cookies.set_cookie(cookie)

        
        if self.trust_env:
            
            env_proxies = get_environ_proxies(url) or {}
            for (k, v) in env_proxies.items():
                proxies.setdefault(k, v)

            
            if not auth:
                auth = get_netrc_auth(url)

            
            if not verify and verify is not False:
                verify = os.environ.get('REQUESTS_CA_BUNDLE')

            
            if not verify and verify is not False:
                verify = os.environ.get('CURL_CA_BUNDLE')


        
        params = merge_kwargs(params, self.params)
        headers = merge_kwargs(headers, self.headers)
        auth = merge_kwargs(auth, self.auth)
        proxies = merge_kwargs(proxies, self.proxies)
        hooks = merge_kwargs(hooks, self.hooks)
        stream = merge_kwargs(stream, self.stream)
        verify = merge_kwargs(verify, self.verify)
        cert = merge_kwargs(cert, self.cert)


        
        req = Request()
        req.method = method
        req.url = url
        req.headers = headers
        req.files = files
        req.data = data
        req.params = params
        req.auth = auth
        req.cookies = cookies
        req.hooks = hooks

        
        prep = req.prepare()

        
        resp = self.send(prep, stream=stream, timeout=timeout, verify=verify, cert=cert, proxies=proxies)

        
        for cookie in resp.cookies:
            self.cookies.set_cookie(cookie)

        
        gen = self.resolve_redirects(resp, req, stream=stream, timeout=timeout, verify=verify, cert=cert, proxies=proxies)

        
        history = [r for r in gen] if allow_redirects else []

        
        if history:
            history.insert(0, resp)
            resp = history.pop()
            resp.history = tuple(history)

        
        self.response = dispatch_hook('response', hooks, resp)

        return resp

    def get(self, url, **kwargs):
        

        kwargs.setdefault('allow_redirects', True)
        return self.request('GET', url, **kwargs)

    def options(self, url, **kwargs):
        

        kwargs.setdefault('allow_redirects', True)
        return self.request('OPTIONS', url, **kwargs)

    def head(self, url, **kwargs):
        

        kwargs.setdefault('allow_redirects', False)
        return self.request('HEAD', url, **kwargs)

    def post(self, url, data=None, **kwargs):
        

        return self.request('POST', url, data=data, **kwargs)

    def put(self, url, data=None, **kwargs):
        

        return self.request('PUT', url, data=data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        

        return self.request('PATCH', url,  data=data, **kwargs)

    def delete(self, url, **kwargs):
        

        return self.request('DELETE', url, **kwargs)

    def send(self, request, **kwargs):
        
        adapter = self.get_adapter(url=request.url)
        r = adapter.send(request, **kwargs)
        return r

    def get_adapter(self, url):
        
        for (prefix, adapter) in self.adapters.items():

            if url.startswith(prefix):
                return adapter

        
        raise InvalidSchema("N"o" "c"o"n"n"e"c"t"i"o"n" "a"d"a"p"t"e"r"s" "w"e"r"e" "f"o"u"n"d" "f"o"r" "'"%"s"'"" ""%"" ""u""r""l"")""
""
"" "" "" "" ""d""e""f"" ""c""l""o""s""e""(""s""e""l""f"")"":""
"" "" "" "" "" "" "" "" 
        for _, v in self.adapters.items():
            v.close()

    def mount(self, prefix, adapter):
        
        self.adapters[prefix] = adapter

    def __getstate__(self):
        return dict((attr, getattr(self, attr, None)) for attr in self.__attrs__)

    def __setstate__(self, state):
        for attr, value in state.items():
            setattr(self, attr, value)


def session():
    

    return Session()
