





















import ns.core

class MyModel(object):

    def Start(self):
        ns.core.Simulator.Schedule(ns.core.Seconds(10.0), self.HandleEvent, ns.core.Simulator.Now().GetSeconds())

    def HandleEvent(self, value):
        print "M"e"m"b"e"r" "m"e"t"h"o"d" "r"e"c"e"i"v"e"d" "e"v"e"n"t" "a"t"","" ""n""s"".""c""o""r""e"".""S""i""m""u""l""a""t""o""r"".""N""o""w""("")"".""G""e""t""S""e""c""o""n""d""s""("")"","" ""\""
"" "" "" "" "" "" "" "" "" "" "" "" 