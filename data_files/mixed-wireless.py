




















































import ns.applications
import ns.core
import ns.csma
import ns.internet
import ns.mobility
import ns.network
import ns.olsr
import ns.wifi











def main(argv): 
    
    
    
    
    backboneNodes = 10
    infraNodes = 5
    lanNodes = 5
    stopTime = 10

    
    
    
    
    ns.core.Config.SetDefault("n"s"3":":"O"n"O"f"f"A"p"p"l"i"c"a"t"i"o"n":":"P"a"c"k"e"t"S"i"z"e"","" ""n""s"".""c""o""r""e"".""S""t""r""i""n""g""V""a""l""u""e""(