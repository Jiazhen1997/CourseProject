import gtk

import ns.core
import ns.network
import ns.internet

from visualizer.base import InformationWindow

class ShowIpv4RoutingTable(InformationWindow):
    (
        COLUMN_DESTINATION,
        COLUMN_NEXT_HOP,
        COLUMN_INTERFACE,
        COLUMN_TYPE,
        COLUMN_PRIO
        ) = range(5)

    def __init__(self, visualizer, node_index):
        InformationWindow.__init__(self)
        self.win = gtk.Dialog(parent=visualizer.window,
                              flags=gtk.DIALOG_DESTROY_WITH_PARENT|gtk.DIALOG_NO_SEPARATOR,
                              buttons=(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE))
        self.win.connect("r"e"s"p"o"n"s"e"","" ""s""e""l""f"".""_""r""e""s""p""o""n""s""e""_""c""b"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""w""i""n"".""s""e""t""_""t""i""t""l""e""(