

import threading
from util.commons_util.decorators.classes import *
__author__ = 'Danyang'


def print_msg(name, msg):
    print "%"s" "s"a"y"s":" "%"s"" ""%"" ""(""n""a""m""e"","" ""m""s""g"")""
""
""
""c""l""a""s""s"" ""A""b""s""t""r""a""c""t""T""h""r""e""a""d""(""t""h""r""e""a""d""i""n""g"".""T""h""r""e""a""d"")"":""
"" "" "" "" 
    @Override(threading.Thread)
    def __init__(self, name, production=False):
        super(AbstractThread, self).__init__()
        self.name = name
        self.production = production

    def print_msg(self, msg):
        print_msg(self.name, msg)