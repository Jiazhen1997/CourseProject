





























import ns.applications
import ns.bridge
import ns.core
import ns.csma
import ns.internet
import ns.network


def main(argv):

    
    
    
    
    cmd = ns.core.CommandLine()
    cmd.Parse(argv)

    
    
    
    
    terminals = ns.network.NodeContainer()
    terminals.Create(4)

    csmaSwitch = ns.network.NodeContainer()
    csmaSwitch.Create(1)

    
    csma = ns.csma.CsmaHelper()
    csma.SetChannelAttribute("D"a"t"a"R"a"t"e"","" ""n""s"".""n""e""t""w""o""r""k"".""D""a""t""a""R""a""t""e""V""a""l""u""e""(""n""s"".""n""e""t""w""o""r""k"".""D""a""t""a""R""a""t""e""(""5""0""0""0""0""0""0"")"")"")""
"" "" "" "" ""c""s""m""a"".""S""e""t""C""h""a""n""n""e""l""A""t""t""r""i""b""u""t""e""(