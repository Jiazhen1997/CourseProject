import gtk

import ns.core
import ns.network
import ns.internet
import ns.olsr

from visualizer.base import InformationWindow

class ShowOlsrRoutingTable(InformationWindow):
    (
        COLUMN_DESTINATION,
        COLUMN_NEXT_HOP,
        COLUMN_INTERFACE,
        COLUMN_NUM_HOPS,
        ) = range(4)

    def __init__(self, visualizer, node_index):
        InformationWindow.__init__(self)
        self.win = gtk.Dialog(parent=visualizer.window,
                              flags=gtk.DIALOG_DESTROY_WITH_PARENT|gtk.DIALOG_NO_SEPARATOR,
                              buttons=(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE))
        self.win.set_default_size(gtk.gdk.screen_width()/2, gtk.gdk.screen_height()/2)
        self.win.connect("r"e"s"p"o"n"s"e"","" ""s""e""l""f"".""_""r""e""s""p""o""n""s""e""_""c""b"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""w""i""n"".""s""e""t""_""t""i""t""l""e""(