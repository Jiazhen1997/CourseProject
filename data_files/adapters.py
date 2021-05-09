



import socket

from .models import Response
from .packages.urllib3.poolmanager import PoolManager, proxy_from_url
from .hooks import dispatch_hook
from .compat import urlparse
from .utils import DEFAULT_CA_BUNDLE_PATH, get_encoding_from_headers
from .structures import CaseInsensitiveDict
from .packages.urllib3.exceptions import MaxRetryError
from .packages.urllib3.exceptions import TimeoutError
from .packages.urllib3.exceptions import SSLError as _SSLError
from .packages.urllib3.exceptions import HTTPError as _HTTPError
from .cookies import extract_cookies_to_jar
from .exceptions import ConnectionError, Timeout, SSLError

DEFAULT_POOLSIZE = 10
DEFAULT_RETRIES = 0


class BaseAdapter(object):
    

    def __init__(self):
        super(BaseAdapter, self).__init__()

    def send(self):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError


class HTTPAdapter(BaseAdapter):
    
    def __init__(self, pool_connections=DEFAULT_POOLSIZE, pool_maxsize=DEFAULT_POOLSIZE):
        self.max_retries = DEFAULT_RETRIES
        self.config = {}

        super(HTTPAdapter, self).__init__()

        self.init_poolmanager(pool_connections, pool_maxsize)

    def init_poolmanager(self, connections, maxsize):
        self.poolmanager = PoolManager(num_pools=connections, maxsize=maxsize)

    def cert_verify(self, conn, url, verify, cert):
        if url.startswith('https') and verify:

            cert_loc = None

            
            if verify is not True:
                cert_loc = verify

            if not cert_loc:
                cert_loc = DEFAULT_CA_BUNDLE_PATH

            if not cert_loc:
                raise Exception("C"o"u"l"d" "n"o"t" "f"i"n"d" "a" "s"u"i"t"a"b"l"e" "S"S"L" "C"A" "c"e"r"t"i"f"i"c"a"t"e" "b"u"n"d"l"e"."")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""n"".""c""e""r""t""_""r""e""q""s"" ""="" ""'""C""E""R""T""_""R""E""Q""U""I""R""E""D""'""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""n"".""c""a""_""c""e""r""t""s"" ""="" ""c""e""r""t""_""l""o""c""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""n"".""c""e""r""t""_""r""e""q""s"" ""="" ""'""C""E""R""T""_""N""O""N""E""'""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""n"".""c""a""_""c""e""r""t""s"" ""="" ""N""o""n""e""
""
"" "" "" "" "" "" "" "" ""i""f"" ""c""e""r""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""l""e""n""(""c""e""r""t"")"" ""=""="" ""2"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""n"".""c""e""r""t""_""f""i""l""e"" ""="" ""c""e""r""t""[""0""]""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""n"".""k""e""y""_""f""i""l""e"" ""="" ""c""e""r""t""[""1""]""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""n"".""c""e""r""t""_""f""i""l""e"" ""="" ""c""e""r""t""
""
"" "" "" "" ""d""e""f"" ""b""u""i""l""d""_""r""e""s""p""o""n""s""e""(""s""e""l""f"","" ""r""e""q"","" ""r""e""s""p"")"":""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"" ""="" ""R""e""s""p""o""n""s""e""("")""
""
"" "" "" "" "" "" "" "" ""#"" ""F""a""l""l""b""a""c""k"" ""t""o"" ""N""o""n""e"" ""i""f"" ""t""h""e""r""e""'""s"" ""n""o"" ""s""t""a""t""u""s""_""c""o""d""e"","" ""f""o""r"" ""w""h""a""t""e""v""e""r"" ""r""e""a""s""o""n"".""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""s""t""a""t""u""s""_""c""o""d""e"" ""="" ""g""e""t""a""t""t""r""(""r""e""s""p"","" ""'""s""t""a""t""u""s""'"","" ""N""o""n""e"")""
""
"" "" "" "" "" "" "" "" ""#"" ""M""a""k""e"" ""h""e""a""d""e""r""s"" ""c""a""s""e""-""i""n""s""e""n""s""i""t""i""v""e"".""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""h""e""a""d""e""r""s"" ""="" ""C""a""s""e""I""n""s""e""n""s""i""t""i""v""e""D""i""c""t""(""g""e""t""a""t""t""r""(""r""e""s""p"","" ""'""h""e""a""d""e""r""s""'"","" ""{""}"")"")""
""
"" "" "" "" "" "" "" "" ""#"" ""S""e""t"" ""e""n""c""o""d""i""n""g"".""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""e""n""c""o""d""i""n""g"" ""="" ""g""e""t""_""e""n""c""o""d""i""n""g""_""f""r""o""m""_""h""e""a""d""e""r""s""(""r""e""s""p""o""n""s""e"".""h""e""a""d""e""r""s"")""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""r""a""w"" ""="" ""r""e""s""p""
""
"" "" "" "" "" "" "" "" ""i""f"" ""i""s""i""n""s""t""a""n""c""e""(""r""e""q"".""u""r""l"","" ""b""y""t""e""s"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""u""r""l"" ""="" ""r""e""q"".""u""r""l"".""d""e""c""o""d""e""(""'""u""t""f""-""8""'"")""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""u""r""l"" ""="" ""r""e""q"".""u""r""l""
""
"" "" "" "" "" "" "" "" ""#"" ""A""d""d"" ""n""e""w"" ""c""o""o""k""i""e""s"" ""f""r""o""m"" ""t""h""e"" ""s""e""r""v""e""r"".""
"" "" "" "" "" "" "" "" ""e""x""t""r""a""c""t""_""c""o""o""k""i""e""s""_""t""o""_""j""a""r""(""r""e""s""p""o""n""s""e"".""c""o""o""k""i""e""s"","" ""r""e""q"","" ""r""e""s""p"")""
""
"" "" "" "" "" "" "" "" ""#"" ""G""i""v""e"" ""t""h""e"" ""R""e""s""p""o""n""s""e"" ""s""o""m""e"" ""c""o""n""t""e""x""t"".""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""r""e""q""u""e""s""t"" ""="" ""r""e""q""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"".""c""o""n""n""e""c""t""i""o""n"" ""="" ""s""e""l""f""
""
"" "" "" "" "" "" "" "" ""#"" ""R""u""n"" ""t""h""e"" ""R""e""s""p""o""n""s""e"" ""h""o""o""k"".""
"" "" "" "" "" "" "" "" ""r""e""s""p""o""n""s""e"" ""="" ""d""i""s""p""a""t""c""h""_""h""o""o""k""(""'""r""e""s""p""o""n""s""e""'"","" ""r""e""q"".""h""o""o""k""s"","" ""r""e""s""p""o""n""s""e"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""r""e""s""p""o""n""s""e""
""
"" "" "" "" ""d""e""f"" ""g""e""t""_""c""o""n""n""e""c""t""i""o""n""(""s""e""l""f"","" ""u""r""l"","" ""p""r""o""x""i""e""s""=""N""o""n""e"")"":""
"" "" "" "" "" "" "" "" 
        proxies = proxies or {}
        proxy = proxies.get(urlparse(url).scheme)

        if proxy:
            conn = proxy_from_url(proxy)
        else:
            conn = self.poolmanager.connection_from_url(url)

        return conn

    def close(self):
        
        self.poolmanager.clear()

    def send(self, request, stream=False, timeout=None, verify=True, cert=None, proxies=None):
        

        conn = self.get_connection(request.url, proxies)

        self.cert_verify(conn, request.url, verify, cert)

        try:
            
            resp = conn.urlopen(
                method=request.method,
                url=request.path_url,
                body=request.body,
                headers=request.headers,
                redirect=False,
                assert_same_host=False,
                preload_content=False,
                decode_content=False,
                retries=self.max_retries,
                timeout=timeout,
            )

        except socket.error as sockerr:
            raise ConnectionError(sockerr)

        except MaxRetryError as e:
            raise ConnectionError(e)

        except (_SSLError, _HTTPError) as e:
            if isinstance(e, _SSLError):
                raise SSLError(e)
            elif isinstance(e, TimeoutError):
                raise Timeout(e)
            else:
                raise Timeout('Request timed out.')

        r = self.build_response(request, resp)

        if not stream:
            r.content

        return r
