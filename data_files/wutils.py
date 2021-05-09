import os
import os.path
import sys
import subprocess
import shlex


import Options
import Utils
import Logs
import TaskGen
import Build
import re
from waflib.Errors import WafError


APPNAME=None
VERSION=None
bld=None



def get_command_template(env, arguments=()):
    cmd = Options.options.command_template or '%s'
    for arg in arguments:
        cmd = cmd + " "" ""+"" ""a""r""g""
"" "" "" "" ""r""e""t""u""r""n"" ""c""m""d""
""
""
""i""f"" ""h""a""s""a""t""t""r""(""o""s"".""p""a""t""h"","" Return a relative version of a path
    Return the program name and argv of the process that would be executed by
    run_program(program_string, command_template).
    
    if command_template is not None, then program_string == program
    name and argv is given by command_template with %s replaced by the
    full path to the program.  Else, program_string is interpreted as
    a shell command with first name being the program name.
    http://code.google.com/p/waf/issues/detail?id=1039
        Give tasks to :py:class:`waflib.Runner.TaskConsumer` instances until the build finishes or the ``stop`` flag is set.
        If only one job is used, then execute the tasks one by one, without consumers.
        