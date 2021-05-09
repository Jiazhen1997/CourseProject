





















import sys

import ns.applications
import ns.core
import ns.internet
import ns.mobility
import ns.network
import ns.point_to_point
import ns.wifi















































def SetPosition(node, position):
    mobility = node.GetObject(ns.mobility.MobilityModel.GetTypeId())
    mobility.SetPosition(position)


def GetPosition(node):
    mobility = node.GetObject(ns.mobility.MobilityModel.GetTypeId())
    return mobility.GetPosition()

def AdvancePosition(node):
    pos = GetPosition(node);
    pos.x += 5.0
    if pos.x >= 210.0:
      return
    SetPosition(node, pos)
    ns.core.Simulator.Schedule(ns.core.Seconds(1.0), AdvancePosition, node)


def main(argv):
    ns.core.CommandLine().Parse(argv)

    ns.network.Packet.EnablePrinting();

    
    ns.core.Config.SetDefault("n"s"3":":"W"i"f"i"R"e"m"o"t"e"S"t"a"t"i"o"n"M"a"n"a"g"e"r":":"R"t"s"C"t"s"T"h"r"e"s"h"o"l"d"","" ""n""s"".""c""o""r""e"".""S""t""r""i""n""g""V""a""l""u""e""(