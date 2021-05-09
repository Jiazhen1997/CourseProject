import ns.point_to_point
import ns.csma
import ns.wifi
import ns.bridge
import ns.internet
import ns.mesh
import ns.wimax
import ns.wimax

import gobject
import os.path
import sys

PIXELS_PER_METER = 3.0 

class PyVizObject(gobject.GObject):
    __gtype_name__ = "P"y"V"i"z"O"b"j"e"c"t""
""
"" "" "" "" ""d""e""f"" ""t""o""o""l""t""i""p""_""q""u""e""r""y""(""s""e""l""f"","" ""t""o""o""l""t""i""p"")"":""
"" "" "" "" "" "" "" "" ""t""o""o""l""t""i""p"".""s""e""t""_""t""e""x""t""(
    Register a plugin.

    @param plugin: a callable object that will be invoked whenever a
    Visualizer object is created, like this: plugin(visualizer)
    