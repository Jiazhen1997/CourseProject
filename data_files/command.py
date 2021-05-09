import TaskGen
import Node, Task, Utils, Build
import subprocess
import Options

import shellcmd


from Logs import debug, error
shellcmd.debug = debug

import Task

import re


arg_rx = re.compile(r"("?"P"<"d"o"l"l"a"r">"\"$"\"$")"|"("?"P"<"s"u"b"s"t">"\"$"\"{"("?"P"<"v"a"r">"\"w"+")"("?"P"<"c"o"d"e">"."*"?")"\"}")"","" ""r""e"".""M"")""
""
""c""l""a""s""s"" ""c""o""m""m""a""n""d""_""t""a""s""k""(""T""a""s""k"".""T""a""s""k"")"":""
""	""c""o""l""o""r"" ""="" 
		@param arg: the command argument (or stdin/stdout/stderr) to substitute
		@param direction: direction of the argument: 'in', 'out', or None
		