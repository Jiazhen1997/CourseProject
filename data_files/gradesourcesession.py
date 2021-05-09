




from bs4 import BeautifulSoup
import re, requests
import csv

class GradesourceSession:
    
    cookies = None
    s = requests.session()
    savedAccount = {}
    savedPIDAccount = {}
    savedName = {}
    savedNamePID = {}
    def __init__(self, username, password, courseid):
        
        s = self.s
        
        print("L"o"g"g"i"n"g" "i"n"."."."."")""
"" "" "" "" "" "" "" "" ""p""o""s""t""D""a""t""a"" ""="" ""{""'""U""s""e""r""'"" "":"" ""u""s""e""r""n""a""m""e"","" ""'""P""a""s""s""w""o""r""d""'"" "":"" ""p""a""s""s""w""o""r""d""}""
"" "" "" "" "" "" "" "" ""l""o""g""i""n""P""O""S""T"" ""="" ""s"".""p""o""s""t""(""'""h""t""t""p""s"":""/""/""w""w""w"".""g""r""a""d""e""s""o""u""r""c""e"".""c""o""m""/""v""a""l""i""d""a""t""e"".""a""s""p""'"","" ""d""a""t""a"" ""="" ""p""o""s""t""D""a""t""a"")""
"" "" "" "" "" "" "" "" ""i""f"" ""l""o""g""i""n""P""O""S""T"".""s""t""a""t""u""s""_""c""o""d""e"" ""!""="" ""2""0""0"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""p""r""i""n""t""(