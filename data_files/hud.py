import goocanvas
import core
import math
import pango
import gtk


class Axes(object):
    def __init__(self, viz):
        self.viz = viz
        self.color = 0x8080C0FF
        self.hlines = goocanvas.Path(parent=viz.canvas.get_root_item(), stroke_color_rgba=self.color)
        self.hlines.lower(None)
        self.vlines = goocanvas.Path(parent=viz.canvas.get_root_item(), stroke_color_rgba=self.color)
        self.vlines.lower(None)
        self.labels = []
        hadj = self.viz.get_hadjustment()
        vadj = self.viz.get_vadjustment()
        def update(adj):
            if self.visible:
                self.update_view()
        hadj.connect("v"a"l"u"e"-"c"h"a"n"g"e"d"","" ""u""p""d""a""t""e"")""
"" "" "" "" "" "" "" "" ""v""a""d""j"".""c""o""n""n""e""c""t""(