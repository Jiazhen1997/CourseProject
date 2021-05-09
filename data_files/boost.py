











import sys
import re
from waflib import Utils, Logs
from waflib.Configure import conf
from waflib.Errors import WafError

BOOST_LIBS = ('/usr/lib/x86_64-linux-gnu', '/usr/lib/i386-linux-gnu', '/usr/lib', '/usr/local/lib',
			  '/opt/local/lib', '/sw/lib', '/lib')
BOOST_INCLUDES = ('/usr/include', '/usr/local/include',
				  '/opt/local/include', '/sw/include')
BOOST_VERSION_FILE = 'boost/version.hpp'
BOOST_VERSION_CODE = 


PLATFORM = Utils.unversioned_sys_platform()
detect_intel = lambda env: (PLATFORM == 'win32') and 'iw' or 'il'
detect_clang = lambda env: (PLATFORM == 'darwin') and 'clang-darwin' or 'clang'
detect_mingw = lambda env: (re.search('MinGW', env.CXX[0])) and 'mgw' or 'gcc'
BOOST_TOOLSETS = {
	'borland':  'bcb',
	'clang':	detect_clang,
	'como':	 'como',
	'cw':	   'cw',
	'darwin':   'xgcc',
	'edg':	  'edg',
	'g++':	  detect_mingw,
	'gcc':	  detect_mingw,
	'icpc':	 detect_intel,
	'intel':	detect_intel,
	'kcc':	  'kcc',
	'kylix':	'bck',
	'mipspro':  'mp',
	'mingw':	'mgw',
	'msvc':	 'vc',
	'qcc':	  'qcc',
	'sun':	  'sw',
	'sunc++':   'sw',
	'tru64cxx': 'tru',
	'vacpp':	'xlc'
}


def options(opt):
	opt.add_option('--boost-includes', type='string',
				   default='', dest='boost_includes',
				   help=)
	opt.add_option('--boost-libs', type='string',
				   default='', dest='boost_libs',
				   help=)
	opt.add_option('--boost-static', action='store_true',
				   default=False, dest='boost_static',
				   help='link static libraries')
	opt.add_option('--boost-mt', action='store_true',
				   default=False, dest='boost_mt',
				   help='select multi-threaded libraries')
	opt.add_option('--boost-abi', type='string', default='', dest='boost_abi',
				   help=)
	opt.add_option('--boost-toolset', type='string',
				   default='', dest='boost_toolset',
				   help='force a toolset e.g. msvc, vc90, \
						gcc, mingw, mgw45 (default: auto)')
	py_version = '%d%d' % (sys.version_info[0], sys.version_info[1])
	opt.add_option('--boost-python', type='string',
				   default=py_version, dest='boost_python',
				   help='select the lib python with this version \
						(default: %s)' % py_version)


@conf
def __boost_get_version_file(self, dir):
	try:
		return self.root.find_dir(dir).find_node(BOOST_VERSION_FILE)
	except:
		return None


@conf
def boost_get_version(self, dir):
	
	re_but = re.compile('^
	try:
		val = re_but.search(self.__boost_get_version_file(dir).read()).group(1)
	except:
		val = self.check_cxx(fragment=BOOST_VERSION_CODE, includes=[dir],
							 execute=True, define_ret=True)
	return val


@conf
def boost_get_includes(self, *k, **kw):
	includes = k and k[0] or kw.get('includes', None)
	if includes and self.__boost_get_version_file(includes):
		return includes
	for dir in BOOST_INCLUDES:
		if self.__boost_get_version_file(dir):
			return dir
	if includes:
		self.fatal('headers not found in %s' % includes)
	else:
		self.fatal('headers not found, use --boost-includes=/path/to/boost')


@conf
def boost_get_toolset(self, cc):
	toolset = cc
	if not cc:
		build_platform = Utils.unversioned_sys_platform()
		if build_platform in BOOST_TOOLSETS:
			cc = build_platform
		else:
			cc = self.env.CXX_NAME
	if cc in BOOST_TOOLSETS:
		toolset = BOOST_TOOLSETS[cc]
	return isinstance(toolset, str) and toolset or toolset(self.env)


@conf
def __boost_get_libs_path(self, *k, **kw):
	
	if 'files' in kw:
		return self.root.find_dir('.'), Utils.to_list(kw['files'])
	libs = k and k[0] or kw.get('libs', None)
	if libs:
		path = self.root.find_dir(libs)
		files = path.ant_glob('*boost_*')
	if not libs or not files:
		for dir in BOOST_LIBS:
			try:
				path = self.root.find_dir(dir)
				files = path.ant_glob('*boost_*')
				if files:
					break
				path = self.root.find_dir(dir + '64')
				files = path.ant_glob('*boost_*')
				if files:
					break
			except:
				path = None
	if not path:
		if libs:
			self.fatal('libs not found in %s' % libs)
		else:
			self.fatal('libs not found, \
					   use --boost-includes=/path/to/boost/lib')
	return path, files


@conf
def boost_get_libs(self, *k, **kw):
	
	path, files = self.__boost_get_libs_path(**kw)
	t = []
	if kw.get('mt', False):
		t.append('mt')
	if kw.get('abi', None):
		t.append(kw['abi'])
	tags = t and '(-%s)+' % '-'.join(t) or ''
	toolset = '(-%s[0-9]{0,3})+' % self.boost_get_toolset(kw.get('toolset', ''))
	version = '(-%s)+' % self.env.BOOST_VERSION

	def find_lib(re_lib, files):
		for file in files:
			if re_lib.search(file.name):
				return file
		return None

	def format_lib_name(name):
		if name.startswith('lib'):
			name = name[3:]
		return name.split('.')[0]

	libs = []
	for lib in Utils.to_list(k and k[0] or kw.get('lib', None)):
		py = (lib == 'python') and '(-py%s)+' % kw['python'] or ''
		
		for pattern in ['boost_%s%s%s%s%s' % (lib, toolset, tags, py, version),
						'boost_%s%s%s%s' % (lib, tags, py, version),
						'boost_%s%s%s' % (lib, tags, version),
						
						'boost_%s%s%s%s' % (lib, toolset, tags, py),
						'boost_%s%s%s' % (lib, tags, py),
						'boost_%s%s' % (lib, tags)]:
			file = find_lib(re.compile(pattern), files)
			if file:
				libs.append(format_lib_name(file.name))
				break
		else:
			self.fatal('lib %s not found in %s' % (lib, path))

	return path.abspath(), libs


@conf
def check_boost(self, *k, **kw):
	
	if not self.env['CXX']:
		self.fatal('load a c++ compiler first, conf.load("c"o"m"p"i"l"e"r"_"c"x"x"")""'"")""
""
""	""p""a""r""a""m""s"" ""="" ""{""'""l""i""b""'"":"" ""k"" ""a""n""d"" ""k""[""0""]"" ""o""r"" ""k""w"".""g""e""t""(""'""l""i""b""'"","" ""N""o""n""e"")""}""
""	""f""o""r"" ""k""e""y"","" ""v""a""l""u""e"" ""i""n"" ""s""e""l""f"".""o""p""t""i""o""n""s"".""_""_""d""i""c""t""_""_"".""i""t""e""m""s""("")"":""
""	""	""i""f"" ""n""o""t"" ""k""e""y"".""s""t""a""r""t""s""w""i""t""h""(""'""b""o""o""s""t""_""'"")"":""
""	""	""	""c""o""n""t""i""n""u""e""
""	""	""k""e""y"" ""="" ""k""e""y""[""l""e""n""(""'""b""o""o""s""t""_""'"")"":""]""
""	""	""p""a""r""a""m""s""[""k""e""y""]"" ""="" ""v""a""l""u""e"" ""a""n""d"" ""v""a""l""u""e"" ""o""r"" ""k""w"".""g""e""t""(""k""e""y"","" ""'""'"")""
""
""	""v""a""r"" ""="" ""k""w"".""g""e""t""(""'""u""s""e""l""i""b""_""s""t""o""r""e""'"","" ""'""B""O""O""S""T""'"")""
""
""	""s""e""l""f"".""s""t""a""r""t""_""m""s""g""(""'""C""h""e""c""k""i""n""g"" ""b""o""o""s""t"" ""i""n""c""l""u""d""e""s""'"")""
""	""t""r""y"":""
""	""	""s""e""l""f"".""e""n""v""[""'""I""N""C""L""U""D""E""S""_""%""s""'"" ""%"" ""v""a""r""]"" ""="" ""s""e""l""f"".""b""o""o""s""t""_""g""e""t""_""i""n""c""l""u""d""e""s""(""*""*""p""a""r""a""m""s"")""
""	""	""s""e""l""f"".""e""n""v"".""B""O""O""S""T""_""V""E""R""S""I""O""N"" ""="" ""s""e""l""f"".""b""o""o""s""t""_""g""e""t""_""v""e""r""s""i""o""n""(""s""e""l""f"".""e""n""v""[""'""I""N""C""L""U""D""E""S""_""%""s""'"" ""%"" ""v""a""r""]"")""
""	""e""x""c""e""p""t"" ""W""a""f""E""r""r""o""r"":""
""	""	""s""e""l""f"".""e""n""d""_""m""s""g""(