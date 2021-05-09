





import logging
import socket
import errno

from socket import error as SocketError, timeout as SocketTimeout

try: 
    from http.client import HTTPConnection, HTTPException
    from http.client import HTTP_PORT, HTTPS_PORT
except ImportError:
    from httplib import HTTPConnection, HTTPException
    from httplib import HTTP_PORT, HTTPS_PORT

try: 
    from queue import LifoQueue, Empty, Full
except ImportError:
    from Queue import LifoQueue, Empty, Full


try: 
    HTTPSConnection = object
    BaseSSLError = None
    ssl = None

    try: 
        from http.client import HTTPSConnection
    except ImportError:
        from httplib import HTTPSConnection

    import ssl
    BaseSSLError = ssl.SSLError

except (ImportError, AttributeError): 
    pass


from .request import RequestMethods
from .response import HTTPResponse
from .util import get_host, is_connection_dropped, ssl_wrap_socket
from .exceptions import (
    ClosedPoolError,
    EmptyPoolError,
    HostChangedError,
    MaxRetryError,
    SSLError,
    TimeoutError,
)

from .packages.ssl_match_hostname import match_hostname, CertificateError
from .packages import six


xrange = six.moves.xrange

log = logging.getLogger(__name__)

_Default = object()

port_by_scheme = {
    'http': HTTP_PORT,
    'https': HTTPS_PORT,
}




class VerifiedHTTPSConnection(HTTPSConnection):
    
    cert_reqs = None
    ca_certs = None
    ssl_version = None

    def set_cert(self, key_file=None, cert_file=None,
                 cert_reqs='CERT_NONE', ca_certs=None):
        ssl_req_scheme = {
            'CERT_NONE': ssl.CERT_NONE,
            'CERT_OPTIONAL': ssl.CERT_OPTIONAL,
            'CERT_REQUIRED': ssl.CERT_REQUIRED
        }

        self.key_file = key_file
        self.cert_file = cert_file
        self.cert_reqs = ssl_req_scheme.get(cert_reqs) or ssl.CERT_NONE
        self.ca_certs = ca_certs

    def connect(self):
        
        sock = socket.create_connection((self.host, self.port), self.timeout)

        
        
        self.sock = ssl_wrap_socket(sock, self.key_file, self.cert_file,
                                    cert_reqs=self.cert_reqs,
                                    ca_certs=self.ca_certs,
                                    server_hostname=self.host,
                                    ssl_version=self.ssl_version)

        if self.ca_certs:
            match_hostname(self.sock.getpeercert(), self.host)




class ConnectionPool(object):
    

    scheme = None
    QueueCls = LifoQueue

    def __init__(self, host, port=None):
        self.host = host
        self.port = port

    def __str__(self):
        return '%s(host=%r, port=%r)' % (type(self).__name__,
                                         self.host, self.port)


class HTTPConnectionPool(ConnectionPool, RequestMethods):
    

    scheme = 'http'

    def __init__(self, host, port=None, strict=False, timeout=None, maxsize=1,
                 block=False, headers=None):
        ConnectionPool.__init__(self, host, port)
        RequestMethods.__init__(self, headers)

        self.strict = strict
        self.timeout = timeout
        self.pool = self.QueueCls(maxsize)
        self.block = block

        
        for _ in xrange(maxsize):
            self.pool.put(None)

        
        self.num_connections = 0
        self.num_requests = 0

    def _new_conn(self):
        
        self.num_connections += 1
        log.info("S"t"a"r"t"i"n"g" "n"e"w" "H"T"T"P" "c"o"n"n"e"c"t"i"o"n" "("%"d")":" "%"s"" ""%""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""(""s""e""l""f"".""n""u""m""_""c""o""n""n""e""c""t""i""o""n""s"","" ""s""e""l""f"".""h""o""s""t"")"")""
"" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""H""T""T""P""C""o""n""n""e""c""t""i""o""n""(""h""o""s""t""=""s""e""l""f"".""h""o""s""t"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""p""o""r""t""=""s""e""l""f"".""p""o""r""t"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""r""i""c""t""=""s""e""l""f"".""s""t""r""i""c""t"")""
""
"" "" "" "" ""d""e""f"" ""_""g""e""t""_""c""o""n""n""(""s""e""l""f"","" ""t""i""m""e""o""u""t""=""N""o""n""e"")"":""
"" "" "" "" "" "" "" "" 
        conn = None
        try:
            conn = self.pool.get(block=self.block, timeout=timeout)

        except AttributeError: 
            raise ClosedPoolError(self, "P"o"o"l" "i"s" "c"l"o"s"e"d"."")""
""
"" "" "" "" "" "" "" "" ""e""x""c""e""p""t"" ""E""m""p""t""y"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""b""l""o""c""k"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""a""i""s""e"" ""E""m""p""t""y""P""o""o""l""E""r""r""o""r""(""s""e""l""f"",""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" 
        Put a connection back into the pool.

        :param conn:
            Connection object for the current host and port as returned by
            :meth:`._new_conn` or :meth:`._get_conn`.

        If the pool is already full, the connection is closed and discarded
        because we exceeded maxsize. If connections are discarded frequently,
        then maxsize should be increased.

        If the pool is closed, then the connection will be closed and discarded.
        
        Perform a request on a given httplib connection object taken from our
        pool.
        
        Close all pooled connections and disable the pool.
        
        Check if the given ``url`` is a member of the same host as this
        connection pool.
        
        Get a connection from the pool and perform an HTTP request. This is the
        lowest level call for making a request, so you'll need to specify all
        the raw details.

        .. note::

           More commonly, it's appropriate to use a convenience method provided
           by :class:`.RequestMethods`, such as :meth:`request`.

        .. note::

           `release_conn` will only behave as expected if
           `preload_content=False` because we want to make
           `preload_content=False` the default behaviour someday soon without
           breaking backwards compatibility.

        :param method:
            HTTP request method (such as GET, POST, PUT, etc.)

        :param body:
            Data to send in the request body (useful for creating
            POST requests, see HTTPConnectionPool.post_url for
            more convenience).

        :param headers:
            Dictionary of custom headers to send, such as User-Agent,
            If-None-Match, etc. If None, pool headers are used. If provided,
            these headers completely replace any pool-specific headers.

        :param retries:
            Number of retries to allow before raising a MaxRetryError exception.

        :param redirect:
            If True, automatically handle redirects (status codes 301, 302,
            303, 307). Each redirect counts as a retry.

        :param assert_same_host:
            If ``True``, will make sure that the host of the pool requests is
            consistent else will raise HostChangedError. When False, you can
            use the pool on an HTTP proxy and request foreign hosts.

        :param timeout:
            If specified, overrides the default timeout for this one request.

        :param pool_timeout:
            If set and the pool is set to block=True, then this method will
            block for ``pool_timeout`` seconds and raise EmptyPoolError if no
            connection is available within the time period.

        :param release_conn:
            If False, then the urlopen call will not release the connection
            back into the pool once a response is received (but will release if
            you read the entire contents of the response such as when
            `preload_content=True`). This is useful if you're not preloading
            the response's content immediately. You will need to call
            ``r.release_conn()`` on the response ``r`` to return the connection
            back into the pool. If None, it takes the value of
            ``response_kw.get('preload_content', True)``.

        :param \**response_kw:
            Additional parameters are passed to
            :meth:`urllib3.response.HTTPResponse.from_httplib`
        
    Same as :class:`.HTTPConnectionPool`, but HTTPS.

    When Python is compiled with the :mod:`ssl` module, then
    :class:`.VerifiedHTTPSConnection` is used, which *can* verify certificates,
    instead of :class:`httplib.HTTPSConnection`.

    The ``key_file``, ``cert_file``, ``cert_reqs``, ``ca_certs``, and ``ssl_version``
    are only used if :mod:`ssl` is available and are fed into
    :meth:`urllib3.util.ssl_wrap_socket` to upgrade the connection socket into an SSL socket.
    
        Return a fresh :class:`httplib.HTTPSConnection`.
        
    Given a url, return an :class:`.ConnectionPool` instance of its host.

    This is a shortcut for not having to parse out the scheme, host, and port
    of the url before creating an :class:`.ConnectionPool` instance.

    :param url:
        Absolute URL string that must include the scheme. Port is optional.

    :param \**kw:
        Passes additional parameters to the constructor of the appropriate
        :class:`.ConnectionPool`. Useful for specifying things like
        timeout, maxsize, headers, etc.

    Example: ::

        >>> conn = connection_from_url('http://google.com/')
        >>> r = conn.request('GET', '/')
    