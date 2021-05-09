import Logs
import Options
import Utils


class CompilerTraits(object):
	def get_warnings_flags(self, level):
		
		raise NotImplementedError

	def get_optimization_flags(self, level):
		
		raise NotImplementedError

	def get_debug_flags(self, level):
		
		raise NotImplementedError


class GccTraits(CompilerTraits):
	def __init__(self):
		super(GccTraits, self).__init__()
		
		self.warnings_flags = [['-Wall'], ['-Werror'], ['-Wextra']]

	def get_warnings_flags(self, level):
		warnings = []
		for l in range(level):
			if l < len(self.warnings_flags):
				warnings.extend(self.warnings_flags[l])
			else:
				break
		return warnings

	def get_optimization_flags(self, level):
		if level == 0:
			return ['-O0']
		elif level == 1:
			return ['-O']
		elif level == 2:
			return ['-O2']
		elif level == 3:
			return ['-O3']

	def get_debug_flags(self, level):
		if level == 0:
			return (['-g0'], ['NDEBUG'])
		elif level == 1:
			return (['-g'], [])
		elif level >= 2:
			return (['-ggdb', '-g3'], ['_DEBUG'])
		

class IccTraits(CompilerTraits):
	def __init__(self):
		super(IccTraits, self).__init__()
		
		
		self.warnings_flags = [[], [], ['-Wall']]
		
	def get_warnings_flags(self, level):
		warnings = []
		for l in range(level):
			if l < len(self.warnings_flags):
				warnings.extend(self.warnings_flags[l])
			else:
				break
		return warnings

	def get_optimization_flags(self, level):
		if level == 0:
			return ['-O0']
		elif level == 1:
			return ['-O']
		elif level == 2:
			return ['-O2']
		elif level == 3:
			return ['-O3']

	def get_debug_flags(self, level):
		if level == 0:
			return (['-g0'], ['NDEBUG'])
		elif level == 1:
			return (['-g'], [])
		elif level >= 2:
			return (['-ggdb', '-g3'], ['_DEBUG'])
		


class MsvcTraits(CompilerTraits):
	def __init__(self):
		super(MsvcTraits, self).__init__()
		
		self.warnings_flags = [['/W2'], ['/WX'], ['/Wall']]

	def get_warnings_flags(self, level):
		warnings = []
		for l in range(level):
			if l < len(self.warnings_flags):
				warnings.extend(self.warnings_flags[l])
			else:
				break
		return warnings

	def get_optimization_flags(self, level):
		if level == 0:
			return ['/Od']
		elif level == 1:
			return []
		elif level == 2:
			return ['/O2']
		elif level == 3:
			return ['/Ox']

	def get_debug_flags(self, level):
		if level == 0:
			return ([], ['NDEBUG'])
		elif level == 1:
			return (['/ZI', '/RTC1'], [])
		elif level >= 2:
			return (['/ZI', '/RTC1'], ['_DEBUG'])



gcc = GccTraits()
icc = IccTraits()
msvc = MsvcTraits()


compiler_mapping = {
	'gcc': gcc,
	'g++': gcc,
	'msvc': msvc,
	'icc': icc,
	'icpc': icc,
}

profiles = {
	
	'default': [2, 1, 1],
	'debug': [0, 2, 3],
	'release': [3, 1, 0],
	}

default_profile = 'default'

def options(opt):
	assert default_profile in profiles
	opt.add_option('-d', '--build-profile',
		       action='store',
		       default=default_profile,
		       help=("S"p"e"c"i"f"y" "t"h"e" "b"u"i"l"d" "p"r"o"f"i"l"e"." " ""
""	""	""	"" "" "" "" "" 