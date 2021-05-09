












import os, sys
from waflib import Utils, Options, Errors
from waflib.Logs import debug, warn, info, error
from waflib.TaskGen import extension, before_method, after_method, feature
from waflib.Configure import conf

FRAG = 


INST = 


@extension('.py')
def process_py(self, node):
	
	try:
		if not self.bld.is_install:
			return
	except:
		return

	try:
		if not self.install_path:
			return
	except AttributeError:
		self.install_path = '${PYTHONDIR}'

	
	
	def inst_py(ctx):
		install_from = getattr(self, 'install_from', None)
		if install_from:
			install_from = self.path.find_dir(install_from)
		install_pyfile(self, node, install_from)
	self.bld.add_post_fun(inst_py)

def install_pyfile(self, node, install_from=None):
	

	from_node = install_from or node.parent
	tsk = self.bld.install_as(self.install_path + '/' + node.path_from(from_node), node, postpone=False)
	path = tsk.get_install_path()

	if self.bld.is_install < 0:
		info("+" "r"e"m"o"v"i"n"g" "b"y"t"e" "c"o"m"p"i"l"e"d" "p"y"t"h"o"n" "f"i"l"e"s"")""
""	""	""f""o""r"" ""x"" ""i""n"" ""'""c""o""'"":""
""	""	""	""t""r""y"":""
""	""	""	""	""o""s"".""r""e""m""o""v""e""(""p""a""t""h"" ""+"" ""x"")""
""	""	""	""e""x""c""e""p""t"" ""O""S""E""r""r""o""r"":""
""	""	""	""	""p""a""s""s""
""
""	""i""f"" ""s""e""l""f"".""b""l""d"".""i""s""_""i""n""s""t""a""l""l"" "">"" ""0"":""
""	""	""t""r""y"":""
""	""	""	""s""t""1"" ""="" ""o""s"".""s""t""a""t""(""p""a""t""h"")""
""	""	""e""x""c""e""p""t"":""
""	""	""	""e""r""r""o""r""(""'""T""h""e"" ""p""y""t""h""o""n"" ""f""i""l""e"" ""i""s"" ""m""i""s""s""i""n""g"","" ""t""h""i""s"" ""s""h""o""u""l""d"" ""n""o""t"" ""h""a""p""p""e""n""'"")""
""
""	""	""f""o""r"" ""x"" ""i""n"" ""[""'""c""'"","" ""'""o""'""]"":""
""	""	""	""d""o""_""i""n""s""t"" ""="" ""s""e""l""f"".""e""n""v""[""'""P""Y""'"" ""+"" ""x"".""u""p""p""e""r""("")""]""
""	""	""	""t""r""y"":""
""	""	""	""	""s""t""2"" ""="" ""o""s"".""s""t""a""t""(""p""a""t""h"" ""+"" ""x"")""
""	""	""	""e""x""c""e""p""t"" ""O""S""E""r""r""o""r"":""
""	""	""	""	""p""a""s""s""
""	""	""	""e""l""s""e"":""
""	""	""	""	""i""f"" ""s""t""1"".""s""t""_""m""t""i""m""e"" ""<""="" ""s""t""2"".""s""t""_""m""t""i""m""e"":""
""	""	""	""	""	""d""o""_""i""n""s""t"" ""="" ""F""a""l""s""e""
""
""	""	""	""i""f"" ""d""o""_""i""n""s""t"":""
""	""	""	""	""l""s""t"" ""="" ""(""x"" ""=""="" ""'""o""'"")"" ""a""n""d"" ""[""s""e""l""f"".""e""n""v""[""'""P""Y""F""L""A""G""S""_""O""P""T""'""]""]"" ""o""r"" ""[""]""
""	""	""	""	""(""a"","" ""b"","" ""c"")"" ""="" ""(""p""a""t""h"","" ""p""a""t""h"" ""+"" ""x"","" ""t""s""k"".""g""e""t""_""i""n""s""t""a""l""l""_""p""a""t""h""(""d""e""s""t""d""i""r""=""F""a""l""s""e"")"" ""+"" ""x"")""
""	""	""	""	""a""r""g""v"" ""="" ""s""e""l""f"".""e""n""v""[""'""P""Y""T""H""O""N""'""]"" ""+"" ""l""s""t"" ""+"" ""[""'""-""c""'"","" ""I""N""S""T"","" ""a"","" ""b"","" ""c""]""
""	""	""	""	""i""n""f""o""(""'""+"" ""b""y""t""e"" ""c""o""m""p""i""l""i""n""g"" ""%""r""'"" ""%"" ""(""p""a""t""h"" ""+"" ""x"")"")""
""	""	""	""	""r""e""t"" ""="" ""U""t""i""l""s"".""s""u""b""p""r""o""c""e""s""s"".""P""o""p""e""n""(""a""r""g""v"")"".""w""a""i""t""("")""
""	""	""	""	""i""f"" ""r""e""t"":""
""	""	""	""	""	""r""a""i""s""e"" ""E""r""r""o""r""s"".""W""a""f""E""r""r""o""r""(""'""p""y""%""s"" ""c""o""m""p""i""l""a""t""i""o""n"" ""f""a""i""l""e""d"" ""%""r""'"" ""%"" ""(""x"","" ""p""a""t""h"")"")""
""
""@""f""e""a""t""u""r""e""(""'""p""y""'"")""
""d""e""f"" ""f""e""a""t""u""r""e""_""p""y""(""s""e""l""f"")"":""
""	
	pass

@feature('pyext')
@before_method('propagate_uselib_vars', 'apply_link')
@after_method('apply_bundle')
def init_pyext(self):
	
	try:
		if not self.install_path:
			return
	except AttributeError:
		self.install_path = '${PYTHONARCHDIR}'
	self.uselib = self.to_list(getattr(self, 'uselib', []))
	if not 'PYEXT' in self.uselib:
		self.uselib.append('PYEXT')
	
	self.env['cshlib_PATTERN'] = self.env['cxxshlib_PATTERN'] = self.env['macbundle_PATTERN'] = self.env['pyext_PATTERN']

@feature('pyext')
@before_method('apply_link', 'apply_bundle')
def set_bundle(self):
	if sys.platform.startswith('darwin'):
		self.mac_bundle = True

@before_method('propagate_uselib_vars')
@feature('pyembed')
def init_pyembed(self):
	
	self.uselib = self.to_list(getattr(self, 'uselib', []))
	if not 'PYEMBED' in self.uselib:
		self.uselib.append('PYEMBED')

@conf
def get_python_variables(conf, variables, imports=['import sys']):
	
	program = list(imports)
	program.append('')
	for v in variables:
		program.append("p"r"i"n"t"("r"e"p"r"("%"s")")"" ""%"" ""v"")""
""	""o""s""_""e""n""v"" ""="" ""d""i""c""t""(""o""s"".""e""n""v""i""r""o""n"")""
""	""t""r""y"":""
""	""	""d""e""l"" ""o""s""_""e""n""v""[""'""M""A""C""O""S""X""_""D""E""P""L""O""Y""M""E""N""T""_""T""A""R""G""E""T""'""]"" ""#"" ""s""e""e"" ""c""o""m""m""e""n""t""s"" ""i""n"" ""t""h""e"" ""O""S""X"" ""t""o""o""l""
""	""e""x""c""e""p""t"" ""K""e""y""E""r""r""o""r"":""
""	""	""p""a""s""s""
""
""	""t""r""y"":""
""	""	""o""u""t"" ""="" ""c""o""n""f"".""c""m""d""_""a""n""d""_""l""o""g""(""c""o""n""f"".""e""n""v"".""P""Y""T""H""O""N"" ""+"" ""[""'""-""c""'"","" ""'""\""n""'"".""j""o""i""n""(""p""r""o""g""r""a""m"")""]"","" ""e""n""v""=""o""s""_""e""n""v"")""
""	""e""x""c""e""p""t"" ""E""r""r""o""r""s"".""W""a""f""E""r""r""o""r"":""
""	""	""c""o""n""f"".""f""a""t""a""l""(""'""T""h""e"" ""d""i""s""t""u""t""i""l""s"" ""m""o""d""u""l""e"" ""i""s"" ""u""n""u""s""a""b""l""e"":"" ""i""n""s""t""a""l""l"" 
	Check for headers and libraries necessary to extend or embed python by using the module *distutils*.
	On success the environment variables xxx_PYEXT and xxx_PYEMBED are added:

	* PYEXT: for compiling python extensions
	* PYEMBED: for embedding a python interpreter
	
	Check if the python interpreter is found matching a given minimum version.
	minver should be a tuple, eg. to check for python >= 2.4.2 pass (2,4,2) as minver.

	If successful, PYTHON_VERSION is defined as 'MAJOR.MINOR'
	(eg. '2.4') of the actual python version found, and PYTHONDIR is
	defined, pointing to the site-packages directory appropriate for
	this python version, where modules/packages/extensions should be
	installed.

	:param minver: minimum version
	:type minver: tuple of int
	
	Check if the selected python interpreter can import the given python module::

		def configure(conf):
			conf.check_python_module('pygccxml')

	:param module_name: module
	:type module_name: string
	
	Detect the python interpreter
	
	Add the options ``--nopyc`` and ``--nopyo``
	