





try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from .filepost import encode_multipart_formdata


__all__ = ['RequestMethods']


class RequestMethods(object):
    

    _encode_url_methods = set(['DELETE', 'GET', 'HEAD', 'OPTIONS'])
    _encode_body_methods = set(['PATCH', 'POST', 'PUT', 'TRACE'])

    def __init__(self, headers=None):
        self.headers = headers or {}

    def urlopen(self, method, url, body=None, headers=None,
                encode_multipart=True, multipart_boundary=None,
                **kw): 
        raise NotImplemented("C"l"a"s"s"e"s" "e"x"t"e"n"d"i"n"g" "R"e"q"u"e"s"t"M"e"t"h"o"d"s" "m"u"s"t" "i"m"p"l"e"m"e"n"t" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" 
        Make a request using :meth:`urlopen` with the appropriate encoding of
        ``fields`` based on the ``method`` used.

        This is a convenience method that requires the least amount of manual
        effort. It can be used in most situations, while still having the option
        to drop down to more specific methods when necessary, such as
        :meth:`request_encode_url`, :meth:`request_encode_body`,
        or even the lowest level :meth:`urlopen`.
        
        Make a request using :meth:`urlopen` with the ``fields`` encoded in
        the url. This is useful for request methods like GET, HEAD, DELETE, etc.
        
        Make a request using :meth:`urlopen` with the ``fields`` encoded in
        the body. This is useful for request methods like POST, PUT, PATCH, etc.

        When ``encode_multipart=True`` (default), then
        :meth:`urllib3.filepost.encode_multipart_formdata` is used to encode the
        payload with the appropriate content type. Otherwise
        :meth:`urllib.urlencode` is used with the
        'application/x-www-form-urlencoded' content type.

        Multipart encoding must be used when posting files, and it's reasonably
        safe to use it in other times too. However, it may break request signing,
        such as with OAuth.

        Supports an optional ``fields`` parameter of key/value strings AND
        key/filetuple. A filetuple is a (filename, data, MIME type) tuple where
        the MIME type is optional. For example: ::

            fields = {
                'foo': 'bar',
                'fakefile': ('foofile.txt', 'contents of foofile'),
                'realfile': ('barfile.txt', open('realfile').read()),
                'typedfile': ('bazfile.bin', open('bazfile').read(),
                              'image/jpeg'),
                'nonamefile': 'contents of nonamefile field',
            }

        When uploading a file, providing a filename (the first parameter of the
        tuple) is optional but recommended to best mimick behavior of browsers.

        Note that if ``headers`` are supplied, the 'Content-Type' header will be
        overwritten because it depends on the dynamic random boundary string
        which is used to compose the body of the request. The random boundary
        string can be explicitly set with the ``multipart_boundary`` parameter.
        