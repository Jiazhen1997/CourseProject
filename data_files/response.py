





import gzip
import logging
import zlib

from io import BytesIO

from .exceptions import DecodeError
from .packages.six import string_types as basestring


log = logging.getLogger(__name__)


def decode_gzip(data):
    gzipper = gzip.GzipFile(fileobj=BytesIO(data))
    return gzipper.read()


def decode_deflate(data):
    try:
        return zlib.decompress(data)
    except zlib.error:
        return zlib.decompress(data, -zlib.MAX_WBITS)


class HTTPResponse(object):
    

    CONTENT_DECODERS = {
        'gzip': decode_gzip,
        'deflate': decode_deflate,
    }

    def __init__(self, body='', headers=None, status=0, version=0, reason=None,
                 strict=0, preload_content=True, decode_content=True,
                 original_response=None, pool=None, connection=None):
        self.headers = headers or {}
        self.status = status
        self.version = version
        self.reason = reason
        self.strict = strict

        self._decode_content = decode_content
        self._body = body if body and isinstance(body, basestring) else None
        self._fp = None
        self._original_response = original_response

        self._pool = pool
        self._connection = connection

        if hasattr(body, 'read'):
            self._fp = body

        if preload_content and not self._body:
            self._body = self.read(decode_content=decode_content)

    def get_redirect_location(self):
        
        if self.status in [301, 302, 303, 307]:
            return self.headers.get('location')

        return False

    def release_conn(self):
        if not self._pool or not self._connection:
            return

        self._pool._put_conn(self._connection)
        self._connection = None

    @property
    def data(self):
        
        if self._body:
            return self._body

        if self._fp:
            return self.read(cache_content=True)

    def read(self, amt=None, decode_content=None, cache_content=False):
        
        
        
        content_encoding = self.headers.get('content-encoding', '').lower()
        decoder = self.CONTENT_DECODERS.get(content_encoding)
        if decode_content is None:
            decode_content = self._decode_content

        if self._fp is None:
            return

        try:
            if amt is None:
                
                data = self._fp.read()
            else:
                return self._fp.read(amt)

            try:
                if decode_content and decoder:
                    data = decoder(data)
            except (IOError, zlib.error):
                raise DecodeError("R"e"c"e"i"v"e"d" "r"e"s"p"o"n"s"e" "w"i"t"h" "c"o"n"t"e"n"t"-"e"n"c"o"d"i"n"g":" "%"s"," "b"u"t" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" 
        Given an :class:`httplib.HTTPResponse` instance ``r``, return a
        corresponding :class:`urllib3.response.HTTPResponse` object.

        Remaining parameters are passed to the HTTPResponse constructor, along
        with ``original_response=r``.
        