



from __future__ import with_statement



from collections import defaultdict
from os.path import join as join_path
from os.path import split as split_path
from shlex import split as shlex_split
from sys import stderr, stdin
from subprocess import Popen, PIPE

try:
    from argparse import ArgumentParser
except ImportError:
    from os.path import basename
    from sys import path as sys_path
    
    sys_path.append(join_path(basename(__file__), '../server/lib'))
    from argparse import ArgumentParser



UNMERGED_SUFFIXES=['a1', 'a2', 'co', 'rel']

MERGED_SUFFIX='ann'
ARGPARSER = ArgumentParser(description=("M"e"r"g"e" "B"i"o"N"L"P"'"1"1" "S"T" "a"n"n"o"t"a"t"i"o"n"s" ""
"" "" "" "" ""'""i""n""t""o"" ""a"" ""s""i""n""g""l""e"" ""f""i""l""e"","" ""r""e""a""d""s"" ""p""a""t""h""s"" ""f""r""o""m"" ""s""t""d""i""n""'"")"")""
""A""R""G""P""A""R""S""E""R"".""a""d""d""_""a""r""g""u""m""e""n""t""(""'""-""w""'"","" ""'""-""-""n""o""-""w""a""r""n""'"","" ""a""c""t""i""o""n""=""'""s""t""o""r""e""_""t""r""u""e""'"",""
"" "" "" "" "" "" "" "" ""h""e""l""p""=""'""s""u""p""p""r""e""s""s"" ""w""a""r""n""i""n""g""s""'"")""
""#""A""R""G""P""A""R""S""E""R"".""a""d""d""_""a""r""g""u""m""e""n""t""(""'""-""d""'"","" ""'""-""-""d""e""b""u""g""'"","" ""a""c""t""i""o""n""=""'""s""t""o""r""e""_""t""r""u""e""'"",""
""#"" "" "" "" "" "" "" "" ""h""e""l""p""=""'""a""c""t""i""v""a""t""e"" ""a""d""d""i""t""i""o""n""a""l"" ""d""e""b""u""g"" ""o""u""t""p""u""t""'"")""
""#""#""#""
""
""d""e""f"" ""k""e""y""n""a""t""(""s""t""r""i""n""g"")"":""
"" "" "" "" ""'""'""'""
"" "" "" "" ""h""t""t""p"":""/""/""c""o""d""e"".""a""c""t""i""v""e""s""t""a""t""e"".""c""o""m""/""r""e""c""i""p""e""s""/""2""8""5""2""6""4""-""n""a""t""u""r""a""l""-""s""t""r""i""n""g""-""s""o""r""t""i""n""g""/""
"" "" "" "" ""'""'""'""
"" "" "" "" ""i""t"" ""="" ""t""y""p""e""(""1"")""
"" "" "" "" ""r"" ""="" ""[""]""
"" "" "" "" ""f""o""r"" ""c"" ""i""n"" ""s""t""r""i""n""g"":""
"" "" "" "" "" "" "" "" ""i""f"" ""c"".""i""s""d""i""g""i""t""("")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""d"" ""="" ""i""n""t""(""c"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""r"" ""a""n""d"" ""t""y""p""e""("" ""r""[""-""1""]"" "")"" ""=""="" ""i""t"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r""[""-""1""]"" ""="" ""r""[""-""1""]"" ""*"" ""1""0"" ""+"" ""d""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""s""e"":"" ""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""r"".""a""p""p""e""n""d""(""d"")""
"" "" "" "" "" "" "" "" ""e""l""s""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r"".""a""p""p""e""n""d""(""c"".""l""o""w""e""r""("")"")""
"" "" "" "" ""r""e""t""u""r""n"" ""r""
""
""d""e""f"" ""m""a""i""n""(""a""r""g""s"")"":""
"" "" "" "" ""a""r""g""p"" ""="" ""A""R""G""P""A""R""S""E""R"".""p""a""r""s""e""_""a""r""g""s""(""a""r""g""s""[""1"":""]"")""
"" "" "" "" ""#"" ""I""D"" ""i""s"" ""t""h""e"" ""s""t""e""m"" ""o""f"" ""a"" ""f""i""l""e""
"" "" "" "" ""i""d""_""t""o""_""a""n""n""_""f""i""l""e""s"" ""="" ""d""e""f""a""u""l""t""d""i""c""t""(""l""i""s""t"")""
"" "" "" "" ""#"" ""I""n""d""e""x"" ""a""l""l"" ""I""D"";""s"" ""b""e""f""o""r""e"" ""w""e"" ""m""e""r""g""e"" ""s""o"" ""t""h""a""t"" ""w""e"" ""c""a""n"" ""d""o"" ""a"" ""l""i""t""t""l""e"" ""m""a""g""i""c""
"" "" "" "" ""f""o""r"" ""f""i""l""e""_""p""a""t""h"" ""i""n"" ""(""l"".""s""t""r""i""p""("")"" ""f""o""r"" ""l"" ""i""n"" ""s""t""d""i""n"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""a""n""y""(""(""f""i""l""e""_""p""a""t""h"".""e""n""d""s""w""i""t""h""(""s""u""f""f"")"" ""f""o""r"" ""s""u""f""f"" ""i""n"" ""U""N""M""E""R""G""E""D""_""S""U""F""F""I""X""E""S"")"")"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""i""f"" ""n""o""t"" ""a""r""g""p"".""n""o""_""w""a""r""n"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""i""m""p""o""r""t"" ""s""y""s""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""y""s"".""s""t""d""e""r""r"","" ""(""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""'""W""A""R""N""I""N""G"":"" ""i""n""v""a""l""i""d"" ""f""i""l""e"" ""s""u""f""f""i""x"" ""f""o""r"" ""%""s"","" ""i""g""n""o""r""i""n""g""'""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "")"" ""%"" ""(""f""i""l""e""_""p""a""t""h"","" "")""
"" "" "" "" "" "" "" "" "" "" "" "" ""c""o""n""t""i""n""u""e""
"" "" "" "" "" "" "" "" ""
"" "" "" "" "" "" "" "" ""d""i""r""n""a""m""e"","" ""b""a""s""e""n""a""m""e"" ""="" ""s""p""l""i""t""_""p""a""t""h""(""f""i""l""e""_""p""a""t""h"")""
"" "" "" "" "" "" "" "" ""i""d"" ""="" ""j""o""i""n""_""p""a""t""h""(""d""i""r""n""a""m""e"","" ""b""a""s""e""n""a""m""e"".""s""p""l""i""t""(""'"".""'"")""[""0""]"")""
"" "" "" "" "" "" "" "" ""i""d""_""t""o""_""a""n""n""_""f""i""l""e""s""[""i""d""]"".""a""p""p""e""n""d""(""f""i""l""e""_""p""a""t""h"")""
""
"" "" "" "" ""f""o""r"" ""i""d"","" ""a""n""n""_""f""i""l""e""s"" ""i""n"" ""i""d""_""t""o""_""a""n""n""_""f""i""l""e""s"".""i""t""e""r""i""t""e""m""s""("")"":""
"" "" "" "" "" "" "" "" ""#""X""X""X"":"" ""C""h""e""c""k"" ""i""f"" ""o""u""t""p""u""t"" ""f""i""l""e"" ""e""x""i""s""t""s""
"" "" "" "" "" "" "" "" ""l""i""n""e""s"" ""="" ""[""]""
"" "" "" "" "" "" "" "" ""f""o""r"" ""a""n""n""_""f""i""l""e""_""p""a""t""h"" ""i""n"" ""a""n""n""_""f""i""l""e""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""w""i""t""h"" ""o""p""e""n""(""a""n""n""_""f""i""l""e""_""p""a""t""h"","" ""'""r""'"")"" ""a""s"" ""a""n""n""_""f""i""l""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""l""i""n""e"" ""i""n"" ""a""n""n""_""f""i""l""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""l""i""n""e""s"".""a""p""p""e""n""d""(""l""i""n""e"")""
""
"" "" "" "" "" "" "" "" ""w""i""t""h"" ""o""p""e""n""(""i""d"" ""+"" ""'"".""'"" ""+"" ""M""E""R""G""E""D""_""S""U""F""F""I""X"","" ""'""w""'"")"" ""a""s"" ""m""e""r""g""e""d""_""a""n""n""_""f""i""l""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""f""o""r"" ""l""i""n""e"" ""i""n"" ""l""i""n""e""s"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""m""e""r""g""e""d""_""a""n""n""_""f""i""l""e"".""w""r""i""t""e""(""l""i""n""e"")""
""
""i""f"" ""_""_""n""a""m""e""_""_"" ""=""="" ""'""_""_""m""a""i""n""_""_""'"":""
"" "" "" "" ""f""r""o""m"" ""s""y""s"" ""i""m""p""o""r""t"" ""a""r""g""v""
"" "" "" "" ""e""x""i""t""(""m""a""i""n""(""a""r""g""v"")"")""
