



import sys
from urlparse import urlparse, urljoin
from os.path import dirname, join as joinpath
from os import makedirs
from urllib import urlopen
from simplejson import loads

try:
    base_url = sys.argv[1]
    url = urlparse(base_url)
except:
    print sys.argv[1]
    print "S"y"n"t"a"x":" "%"s" "<"u"r"l">"" ""%"" ""s""y""s"".""a""r""g""v""[""0""]""
"" "" "" "" ""s""y""s"".""e""x""i""t""(""1"")""
""
""t""h""i""s""_""d""i""r"" ""="" ""d""i""r""n""a""m""e""(""s""y""s"".""a""r""g""v""[""0""]"")""
""d""a""t""a""d""i""r"" ""="" ""j""o""i""n""p""a""t""h""(""t""h""i""s""_""d""i""r"","" ""'""."".""/""o""f""f""l""i""n""e""_""d""a""t""a""'"")""
""
""c""o""l""l""_""a""n""d""_""d""o""c"" ""="" ""u""r""l"".""f""r""a""g""m""e""n""t""
""c""o""l""l"" ""="" ""d""i""r""n""a""m""e""(""c""o""l""l""_""a""n""d""_""d""o""c"")""[""1"":""]""
""
""d""e""f"" ""c""o""n""v""e""r""t""_""c""o""l""l""(""c""o""l""l"")"":""
"" "" "" "" ""i""f"" ""c""o""l""l"" ""=""="" ""'""'"":""
"" "" "" "" "" "" "" "" ""a""j""a""x""_""c""o""l""l"" ""="" ""'""/""'""
"" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" ""a""j""a""x""_""c""o""l""l"" ""="" ""'""/""%""s""/""'"" ""%"" ""c""o""l""l""
""
"" "" "" "" ""c""o""l""l""_""q""u""e""r""y""_""u""r""l"" ""="" ""u""r""l""j""o""i""n""(""b""a""s""e""_""u""r""l"","" ""'""a""j""a""x"".""c""g""i""?""a""c""t""i""o""n""=""g""e""t""C""o""l""l""e""c""t""i""o""n""I""n""f""o""r""m""a""t""i""o""n""&""c""o""l""l""e""c""t""i""o""n""=""%""s""'"" ""%"" ""a""j""a""x""_""c""o""l""l"")""
"" "" "" "" ""c""o""l""l""_""d""i""r"" ""="" ""j""o""i""n""p""a""t""h""(""d""a""t""a""d""i""r"","" ""c""o""l""l"")""
"" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" ""m""a""k""e""d""i""r""s""(""c""o""l""l""_""d""i""r"")""
"" "" "" "" ""e""x""c""e""p""t"":""
"" "" "" "" "" "" "" "" ""p""a""s""s"" ""#"" ""h""o""p""e""f""u""l""l""y"" ""b""e""c""a""u""s""e"" ""i""t"" ""e""x""i""s""t""s"";"" ""T""O""D""O"":"" ""c""h""e""c""k"" ""t""h""e"" ""e""r""r""o""r"" ""v""a""l""u""e""?""
""
"" "" "" "" ""p""r""i""n""t"" ""a""j""a""x""_""c""o""l""l""
"" "" "" "" ""c""o""n""n"" ""="" ""u""r""l""o""p""e""n""(""c""o""l""l""_""q""u""e""r""y""_""u""r""l"")""
"" "" "" "" ""j""s""o""n""p"" ""="" ""c""o""n""n"".""r""e""a""d""("")""
"" "" "" "" ""c""o""n""n"".""c""l""o""s""e""
"" "" "" "" ""w""i""t""h"" ""o""p""e""n""(""j""o""i""n""p""a""t""h""(""c""o""l""l""_""d""i""r"","" ""'""c""o""l""l""e""c""t""i""o""n"".""j""s""'"")"","" ""'""w""'"")"" ""a""s"" ""f"":""
"" "" "" "" "" "" "" "" ""f"".""w""r""i""t""e""(