





import logging

from ._collections import RecentlyUsedContainer
from .connectionpool import HTTPConnectionPool, HTTPSConnectionPool
from .connectionpool import connection_from_url, port_by_scheme
from .request import RequestMethods
from .util import parse_url


__all__ = ['PoolManager', 'ProxyManager', 'proxy_from_url']


pool_classes_by_scheme = {
    'http': HTTPConnectionPool,
    'https': HTTPSConnectionPool,
}

log = logging.getLogger(__name__)


class PoolManager(RequestMethods):
    

    def __init__(self, num_pools=10, headers=None, **connection_pool_kw):
        RequestMethods.__init__(self, headers)
        self.connection_pool_kw = connection_pool_kw
        self.pools = RecentlyUsedContainer(num_pools,
                                           dispose_func=lambda p: p.close())

    def clear(self):
        
        self.pools.clear()

    def connection_from_host(self, host, port=None, scheme='http'):
        
        port = port or port_by_scheme.get(scheme, 80)

        pool_key = (scheme, host, port)

        
        
        pool = self.pools.get(pool_key)
        if pool:
            return pool

        
        pool_cls = pool_classes_by_scheme[scheme]
        pool = pool_cls(host, port, **self.connection_pool_kw)

        self.pools[pool_key] = pool

        return pool

    def connection_from_url(self, url):
        
        u = parse_url(url)
        return self.connection_from_host(u.host, port=u.port, scheme=u.scheme)

    def urlopen(self, method, url, redirect=True, **kw):
        
        u = parse_url(url)
        conn = self.connection_from_host(u.host, port=u.port, scheme=u.scheme)

        kw['assert_same_host'] = False
        kw['redirect'] = False
        if 'headers' not in kw:
            kw['headers'] = self.headers

        response = conn.urlopen(method, u.request_uri, **kw)

        redirect_location = redirect and response.get_redirect_location()
        if not redirect_location:
            return response

        if response.status == 303:
            method = 'GET'

        log.info("R"e"d"i"r"e"c"t"i"n"g" "%"s" "-">" "%"s"" ""%"" ""(""u""r""l"","" ""r""e""d""i""r""e""c""t""_""l""o""c""a""t""i""o""n"")"")""
"" "" "" "" "" "" "" "" ""k""w""[""'""r""e""t""r""i""e""s""'""]"" ""="" ""k""w"".""g""e""t""(""'""r""e""t""r""i""e""s""'"","" ""3"")"" ""-"" ""1"" "" ""#"" ""P""e""r""s""i""s""t"" ""r""e""t""r""i""e""s"" ""c""o""u""n""t""d""o""w""n""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""u""r""l""o""p""e""n""(""m""e""t""h""o""d"","" ""r""e""d""i""r""e""c""t""_""l""o""c""a""t""i""o""n"","" ""*""*""k""w"")""
""
""
""c""l""a""s""s"" ""P""r""o""x""y""M""a""n""a""g""e""r""(""R""e""q""u""e""s""t""M""e""t""h""o""d""s"")"":""
"" "" "" "" 

    def __init__(self, proxy_pool):
        self.proxy_pool = proxy_pool

    def _set_proxy_headers(self, headers=None):
        headers_ = {'Accept': '*/*'}
        if headers:
            headers_.update(headers)

        return headers_

    def urlopen(self, method, url, **kw):
        "S"a"m"e" "a"s" "H"T"T"P"("S")"C"o"n"n"e"c"t"i"o"n"P"o"o"l"."u"r"l"o"p"e"n"," "`"`"u"r"l"`"`" "m"u"s"t" "b"e" "a"b"s"o"l"u"t"e".""
"" "" "" "" "" "" "" "" ""k""w""[""'""a""s""s""e""r""t""_""s""a""m""e""_""h""o""s""t""'""]"" ""="" ""F""a""l""s""e""
"" "" "" "" "" "" "" "" ""k""w""[""'""h""e""a""d""e""r""s""'""]"" ""="" ""s""e""l""f"".""_""s""e""t""_""p""r""o""x""y""_""h""e""a""d""e""r""s""(""k""w"".""g""e""t""(""'""h""e""a""d""e""r""s""'"")"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""s""e""l""f"".""p""r""o""x""y""_""p""o""o""l"".""u""r""l""o""p""e""n""(""m""e""t""h""o""d"","" ""u""r""l"","" ""*""*""k""w"")""
""
""
""d""e""f"" ""p""r""o""x""y""_""f""r""o""m""_""u""r""l""(""u""r""l"","" ""*""*""p""o""o""l""_""k""w"")"":""
"" "" "" "" ""p""r""o""x""y""_""p""o""o""l"" ""="" ""c""o""n""n""e""c""t""i""o""n""_""f""r""o""m""_""u""r""l""(""u""r""l"","" ""*""*""p""o""o""l""_""k""w"")""
"" "" "" "" ""r""e""t""u""r""n"" ""P""r""o""x""y""M""a""n""a""g""e""r""(""p""r""o""x""y""_""p""o""o""l"")""
