




import os
from waflib import Build, ConfigSet, Task, Utils, Errors
from waflib.TaskGen import feature, before_method, after_method

EXTRA_LOCK = '.old_srcdir'

old1 = Build.BuildContext.store
def store(self):
	old1(self)
	db = os.path.join(self.variant_dir, EXTRA_LOCK)
	env = ConfigSet.ConfigSet()
	env.SRCDIR = self.srcnode.abspath()
	env.store(db)
Build.BuildContext.store = store

old2 = Build.BuildContext.init_dirs
def init_dirs(self):

	if not (os.path.isabs(self.top_dir) and os.path.isabs(self.out_dir)):
		raise Errors.WafError('The project was not configured: run "w"a"f" "c"o"n"f"i"g"u"r"e"" ""f""i""r""s""t""!""'"")""
""
""	""s""r""c""d""i""r"" ""="" ""N""o""n""e""
""	""d""b"" ""="" ""o""s"".""p""a""t""h"".""j""o""i""n""(""s""e""l""f"".""v""a""r""i""a""n""t""_""d""i""r"","" ""E""X""T""R""A""_""L""O""C""K"")""
""	""e""n""v"" ""="" ""C""o""n""f""i""g""S""e""t"".""C""o""n""f""i""g""S""e""t""("")""
""	""t""r""y"":""
""	""	""e""n""v"".""l""o""a""d""(""d""b"")""
""	""	""s""r""c""d""i""r"" ""="" ""e""n""v"".""S""R""C""D""I""R""
""	""e""x""c""e""p""t"":""
""	""	""p""a""s""s""
""
""	""i""f"" ""s""r""c""d""i""r"":""
""	""	""d"" ""="" ""s""e""l""f"".""r""o""o""t"".""f""i""n""d""_""n""o""d""e""(""s""r""c""d""i""r"")""
""	""	""i""f"" ""d"" ""a""n""d"" ""s""r""c""d""i""r"" ""!""="" ""s""e""l""f"".""t""o""p""_""d""i""r"" ""a""n""d"" ""g""e""t""a""t""t""r""(""d"","" ""'""c""h""i""l""d""r""e""n""'"","" ""'""'"")"":""
""	""	""	""s""r""c""n""o""d""e"" ""="" ""s""e""l""f"".""r""o""o""t"".""m""a""k""e""_""n""o""d""e""(""s""e""l""f"".""t""o""p""_""d""i""r"")""
""	""	""	""p""r""i""n""t""(