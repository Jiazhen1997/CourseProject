



import os
import time
import hashlib
import logging

from base64 import b64encode

from .compat import urlparse, str
from .utils import parse_dict_header


log = logging.getLogger(__name__)

CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'
CONTENT_TYPE_MULTI_PART = 'multipart/form-data'


def _basic_auth_str(username, password):
    

    return 'Basic ' + b64encode(('%s:%s' % (username, password)).encode('latin1')).strip().decode('latin1')


class AuthBase(object):
    

    def __call__(self, r):
        raise NotImplementedError('Auth hooks must be callable.')

class HTTPBasicAuth(AuthBase):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self, r):
        r.headers['Authorization'] = _basic_auth_str(self.username, self.password)
        return r


class HTTPProxyAuth(HTTPBasicAuth):
    
    def __call__(self, r):
        r.headers['Proxy-Authorization'] = _basic_auth_str(self.username, self.password)
        return r


class HTTPDigestAuth(AuthBase):
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.last_nonce = ''
        self.nonce_count = 0
        self.chal = {}

    def build_digest_header(self, method, url):

        realm = self.chal['realm']
        nonce = self.chal['nonce']
        qop = self.chal.get('qop')
        algorithm = self.chal.get('algorithm', 'MD5')
        opaque = self.chal.get('opaque', None)

        algorithm = algorithm.upper()
        
        if algorithm == 'MD5':
            def md5_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.md5(x).hexdigest()
            hash_utf8 = md5_utf8
        elif algorithm == 'SHA':
            def sha_utf8(x):
                if isinstance(x, str):
                    x = x.encode('utf-8')
                return hashlib.sha1(x).hexdigest()
            hash_utf8 = sha_utf8
        
        KD = lambda s, d: hash_utf8("%"s":"%"s"" ""%"" ""(""s"","" ""d"")"")""
""
"" "" "" "" "" "" "" "" ""i""f"" ""h""a""s""h""_""u""t""f""8"" ""i""s"" ""N""o""n""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n"" ""N""o""n""e""
""
"" "" "" "" "" "" "" "" ""#"" ""X""X""X"" ""n""o""t"" ""i""m""p""l""e""m""e""n""t""e""d"" ""y""e""t""
"" "" "" "" "" "" "" "" ""e""n""t""d""i""g"" ""="" ""N""o""n""e""
"" "" "" "" "" "" "" "" ""p""_""p""a""r""s""e""d"" ""="" ""u""r""l""p""a""r""s""e""(""u""r""l"")""
"" "" "" "" "" "" "" "" ""p""a""t""h"" ""="" ""p""_""p""a""r""s""e""d"".""p""a""t""h""
"" "" "" "" "" "" "" "" ""i""f"" ""p""_""p""a""r""s""e""d"".""q""u""e""r""y"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""a""t""h"" ""+""="" ""'""?""'"" ""+"" ""p""_""p""a""r""s""e""d"".""q""u""e""r""y""
""
"" "" "" "" "" "" "" "" ""A""1"" ""="" ""'""%""s"":""%""s"":""%""s""'"" ""%"" ""(""s""e""l""f"".""u""s""e""r""n""a""m""e"","" ""r""e""a""l""m"","" ""s""e""l""f"".""p""a""s""s""w""o""r""d"")""
"" "" "" "" "" "" "" "" ""A""2"" ""="" ""'""%""s"":""%""s""'"" ""%"" ""(""m""e""t""h""o""d"","" ""p""a""t""h"")""
""
"" "" "" "" "" "" "" "" ""i""f"" ""q""o""p"" ""=""="" ""'""a""u""t""h""'"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""n""o""n""c""e"" ""=""="" ""s""e""l""f"".""l""a""s""t""_""n""o""n""c""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""n""o""n""c""e""_""c""o""u""n""t"" ""+""="" ""1""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""n""o""n""c""e""_""c""o""u""n""t"" ""="" ""1""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""c""v""a""l""u""e"" ""="" ""'""%""0""8""x""'"" ""%"" ""s""e""l""f"".""n""o""n""c""e""_""c""o""u""n""t""
"" "" "" "" "" "" "" "" "" "" "" "" ""s"" ""="" ""s""t""r""(""s""e""l""f"".""n""o""n""c""e""_""c""o""u""n""t"")"".""e""n""c""o""d""e""(""'""u""t""f""-""8""'"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s"" ""+""="" ""n""o""n""c""e"".""e""n""c""o""d""e""(""'""u""t""f""-""8""'"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s"" ""+""="" ""t""i""m""e"".""c""t""i""m""e""("")"".""e""n""c""o""d""e""(""'""u""t""f""-""8""'"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""s"" ""+""="" ""o""s"".""u""r""a""n""d""o""m""(""8"")""
""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""n""o""n""c""e"" ""="" ""(""h""a""s""h""l""i""b"".""s""h""a""1""(""s"")"".""h""e""x""d""i""g""e""s""t""("")""["":""1""6""]"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""n""o""n""c""e""b""i""t"" ""="" Takes the given response and tries digest-auth, if needed.