


import Options
import Configure
import subprocess
import config_c
import sys

def configure(conf):
	pkg_config = conf.find_program('pkg-config', var='PKG_CONFIG')
	if not pkg_config: return

@Configure.conf
def pkg_check_modules(conf, uselib_name, expression, mandatory=True):
	pkg_config = conf.env['PKG_CONFIG']
	if not pkg_config:
		if mandatory:
			conf.fatal("p"k"g"-"c"o"n"f"i"g" "i"s" "n"o"t" "a"v"a"i"l"a"b"l"e"")""
""	""	""e""l""s""e"":""
""	""	""	""r""e""t""u""r""n"" ""F""a""l""s""e""
""
""	""i""f"" ""O""p""t""i""o""n""s"".""o""p""t""i""o""n""s"".""v""e""r""b""o""s""e"":""
""	""	""e""x""t""r""a""_""m""s""g"" ""="" ""'"" ""(""%""s"")""'"" ""%"" ""e""x""p""r""e""s""s""i""o""n""
""	""e""l""s""e"":""
""	""	""e""x""t""r""a""_""m""s""g"" ""="" ""'""'""
""
""	""c""o""n""f"".""s""t""a""r""t""_""m""s""g""(""'""C""h""e""c""k""i""n""g"" ""f""o""r"" ""p""k""g""-""c""o""n""f""i""g"" ""f""l""a""g""s"" ""f""o""r"" ""%""s""%""s""'"" ""%"" ""(""u""s""e""l""i""b""_""n""a""m""e"","" ""e""x""t""r""a""_""m""s""g"")"")""
""
""	""a""r""g""v"" ""="" ""[""p""k""g""_""c""o""n""f""i""g"","" ""'""-""-""c""f""l""a""g""s""'"","" ""'""-""-""l""i""b""s""'"","" ""e""x""p""r""e""s""s""i""o""n""]""
""	""c""m""d"" ""="" ""s""u""b""p""r""o""c""e""s""s"".""P""o""p""e""n""(""a""r""g""v"","" ""s""t""d""o""u""t""=""s""u""b""p""r""o""c""e""s""s"".""P""I""P""E"","" ""s""t""d""e""r""r""=""s""u""b""p""r""o""c""e""s""s"".""P""I""P""E"")""
""	""o""u""t"","" ""e""r""r"" ""="" ""c""m""d"".""c""o""m""m""u""n""i""c""a""t""e""("")""
""	""r""e""t""v""a""l"" ""="" ""c""m""d"".""w""a""i""t""("")""
""
""	""c""o""n""f"".""t""o""_""l""o""g""(""'""%""r"":"" ""%""r"" ""(""e""x""i""t"" ""c""o""d""e"" ""%""i"")""\""n""%""s""'"" ""%"" ""(""a""r""g""v"","" ""o""u""t"","" ""r""e""t""v""a""l"","" ""e""r""r"")"")""
""
""	""i""f"" ""r""e""t""v""a""l"" ""!""="" ""0"":""
""	""	""c""o""n""f"".""e""n""d""_""m""s""g""(""F""a""l""s""e"")""
""	""	""s""y""s"".""s""t""d""e""r""r"".""w""r""i""t""e""(""e""r""r"")""
""	""e""l""s""e"":""
""	""	""i""f"" ""O""p""t""i""o""n""s"".""o""p""t""i""o""n""s"".""v""e""r""b""o""s""e"":""
""	""	""	""c""o""n""f"".""e""n""d""_""m""s""g""(""o""u""t"")""
""	""	""e""l""s""e"":""
""	""	""	""c""o""n""f"".""e""n""d""_""m""s""g""(""T""r""u""e"")""
""
""	""i""f"" ""r""e""t""v""a""l"" ""=""="" ""0"":""
""	""	""c""o""n""f"".""p""a""r""s""e""_""f""l""a""g""s""(""o""u""t"","" ""u""s""e""l""i""b""_""n""a""m""e"","" ""c""o""n""f"".""e""n""v"")""
""	""	""c""o""n""f"".""e""n""v""[""u""s""e""l""i""b""_""n""a""m""e""]"" ""="" ""T""r""u""e""
""	""	""r""e""t""u""r""n"" ""T""r""u""e""
""
""	""e""l""s""e"":""
""
""	""	""c""o""n""f"".""e""n""v""[""u""s""e""l""i""b""_""n""a""m""e""]"" ""="" ""F""a""l""s""e""
""	""	""i""f"" ""m""a""n""d""a""t""o""r""y"":""
""	""	""	""r""a""i""s""e"" ""C""o""n""f""i""g""u""r""e"".""C""o""n""f""i""g""u""r""a""t""i""o""n""E""r""r""o""r""(""'""p""k""g""-""c""o""n""f""i""g"" ""c""h""e""c""k"" ""f""a""i""l""e""d""'"")""
""	""	""e""l""s""e"":""
""	""	""	""r""e""t""u""r""n"" ""F""a""l""s""e""
""
""@""C""o""n""f""i""g""u""r""e"".""c""o""n""f""
""d""e""f"" ""p""k""g""_""c""h""e""c""k""_""m""o""d""u""l""e""_""v""a""r""i""a""b""l""e""(""c""o""n""f"","" ""m""o""d""u""l""e"","" ""v""a""r""i""a""b""l""e"")"":""
""	""p""k""g""_""c""o""n""f""i""g"" ""="" ""c""o""n""f"".""e""n""v""[""'""P""K""G""_""C""O""N""F""I""G""'""]""
""	""i""f"" ""n""o""t"" ""p""k""g""_""c""o""n""f""i""g"":""
""	""	""c""o""n""f"".""f""a""t""a""l""(