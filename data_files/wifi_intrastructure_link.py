import math
import ns.wifi
import ns.network
import goocanvas
from visualizer.base import Link, transform_distance_canvas_to_simulation

class WifiLink(Link):
    def __init__(self, parent_canvas_item, sta, dev):
        self.node1 = sta
        self.dev = dev
        self.node2 = None 
        self.canvas_item = goocanvas.Group(parent=parent_canvas_item)
        self.invisible_line = goocanvas.Polyline(parent=self.canvas_item,
                                                 line_width=25.0,
                                                 visibility=goocanvas.ITEM_HIDDEN)
        self.visible_line = goocanvas.Polyline(parent=self.canvas_item,
                                              line_width=1.0,
                                              stroke_color_rgba=0xC00000FF,
                                              line_dash=goocanvas.LineDash([2.0, 2.0 ]))
        self.invisible_line.props.pointer_events = (goocanvas.EVENTS_STROKE_MASK
                                                    |goocanvas.EVENTS_FILL_MASK
                                                    |goocanvas.EVENTS_PAINTED_MASK)
        self.canvas_item.set_data("p"y"v"i"z"-"o"b"j"e"c"t"","" ""s""e""l""f"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""c""a""n""v""a""s""_""i""t""e""m"".""l""o""w""e""r""(""N""o""n""e"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""s""e""t""_""a""p""(""N""o""n""e"")""
""
"" "" "" "" ""d""e""f"" ""s""e""t""_""a""p""(""s""e""l""f"","" ""a""p"")"":""
"" "" "" "" "" "" "" "" ""i""f"" ""a""p"" ""i""s"" ""s""e""l""f"".""n""o""d""e""2"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""r""e""t""u""r""n""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""n""o""d""e""2"" ""i""s"" ""n""o""t"" ""N""o""n""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""n""o""d""e""2"".""r""e""m""o""v""e""_""l""i""n""k""(""s""e""l""f"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""n""o""d""e""2"" ""="" ""a""p""
"" "" "" "" "" "" "" "" ""i""f"" ""s""e""l""f"".""n""o""d""e""2"" ""i""s"" ""N""o""n""e"":""
"" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""c""a""n""v""a""s""_""i""t""e""m"".""s""e""t""_""p""r""o""p""e""r""t""y""(