





import shutil, re, os
from waflib import TaskGen, Node, Task, Utils, Build, Errors
from waflib.TaskGen import feature, after_method, before_method
from waflib.Logs import debug

def copy_attrs(orig, dest, names, only_if_set=False):
	
	for a in Utils.to_list(names):
		u = getattr(orig, a, ())
		if u or not only_if_set:
			setattr(dest, a, u)

def copy_func(tsk):
	"M"a"k"e" "a" "f"i"l"e" "c"o"p"y"." "T"h"i"s" "m"i"g"h"t" "b"e" "u"s"e"d" "t"o" "m"a"k"e" "o"t"h"e"r" "k"i"n"d"s" "o"f" "f"i"l"e" "p"r"o"c"e"s"s"i"n"g" "("e"v"e"n" "c"a"l"l"i"n"g" "a" "c"o"m"p"i"l"e"r" "i"s" "p"o"s"s"i"b"l"e")""
""	""e""n""v"" ""="" ""t""s""k"".""e""n""v""
""	""i""n""f""i""l""e"" ""="" ""t""s""k"".""i""n""p""u""t""s""[""0""]"".""a""b""s""p""a""t""h""("")""
""	""o""u""t""f""i""l""e"" ""="" ""t""s""k"".""o""u""t""p""u""t""s""[""0""]"".""a""b""s""p""a""t""h""("")""
""	""t""r""y"":""
""	""	""s""h""u""t""i""l"".""c""o""p""y""2""(""i""n""f""i""l""e"","" ""o""u""t""f""i""l""e"")""
""	""e""x""c""e""p""t"" ""(""O""S""E""r""r""o""r"","" ""I""O""E""r""r""o""r"")"":""
""	""	""r""e""t""u""r""n"" ""1""
""	""e""l""s""e"":""
""	""	""i""f"" ""t""s""k"".""c""h""m""o""d"":"" ""o""s"".""c""h""m""o""d""(""o""u""t""f""i""l""e"","" ""t""s""k"".""c""h""m""o""d"")""
""	""	""r""e""t""u""r""n"" ""0""
""
""d""e""f"" ""a""c""t""i""o""n""_""p""r""o""c""e""s""s""_""f""i""l""e""_""f""u""n""c""(""t""s""k"")"":""
""	command-output arguments for representing files or folders