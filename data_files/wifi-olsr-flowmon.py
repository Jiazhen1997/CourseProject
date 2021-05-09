

















import sys

import ns.applications
import ns.core
import ns.flow_monitor
import ns.internet
import ns.mobility
import ns.network
import ns.olsr
import ns.wifi

DISTANCE = 100 
NUM_NODES_SIDE = 3

def main(argv):

    cmd = ns.core.CommandLine()

    cmd.NumNodesSide = None
    cmd.AddValue("N"u"m"N"o"d"e"s"S"i"d"e"","" 