















import shlex
import subprocess
import sys
import re
import os

env_var_rx = re.compile(r"^"("["a"-"z"A"-"Z"0"-"9"_"]"+")"="("\"S"+")"$"")""
""
""d""e""f"" ""d""e""b""u""g""(""m""e""s""s""a""g""e"")"":""
"" "" "" "" ""p""r""i""n""t"" "">"">"" ""s""y""s"".""s""t""d""e""r""r"","" ""m""e""s""s""a""g""e""
""
""
""i""f"" ""s""y""s"".""p""l""a""t""f""o""r""m"" ""=""="" ""'""w""i""n""3""2""'"":""
"" "" "" "" ""d""e""v""_""n""u""l""l"" ""="" ""o""p""e""n""(