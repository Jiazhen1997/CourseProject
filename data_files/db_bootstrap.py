


import MySQLdb as mdb
import sys

from datetime import datetime

__author__ = 'Daniel'


def start_stamp(func):
  
  def ret(*args):
    print ("%"s":" "e"x"e"c" "%"s"" ""%"" ""(""s""t""r""(""d""a""t""e""t""i""m""e"".""n""o""w""("")"")"","" ""f""u""n""c"".""_""_""n""a""m""e""_""_"")"")""
"" "" "" "" ""r""e""t""u""r""n"" ""f""u""n""c""(""*""a""r""g""s"")""
""
"" "" ""r""e""t""u""r""n"" ""r""e""t""
""
""
""c""l""a""s""s"" ""C""o""n""n""e""c""t""i""o""n""(""o""b""j""e""c""t"")"":""
"" "" ""d""e""f"" ""_""_""i""n""i""t""_""_""(""s""e""l""f"","" ""d""b""_""n""a""m""e"","" ""d""e""f""a""u""l""t""_""f""i""l""e"")"":""
"" "" "" "" ""p""r""i""n""t"" 