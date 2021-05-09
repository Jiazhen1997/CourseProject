import gobject
import gtk

import ns.core
import ns.network
import ns.visualizer

from visualizer.base import InformationWindow
from visualizer.higcontainer import HIGContainer
from kiwi.ui.objectlist import ObjectList, Column

class ShowLastPackets(InformationWindow):
    class PacketList(gtk.ScrolledWindow):
        (
            COLUMN_TIME,
            COLUMN_INTERFACE,
            COLUMN_SIZE,
            COLUMN_CONTENTS,
            ) = range(4)

        def __init__(self):
            super(ShowLastPackets.PacketList, self).__init__()
            self.set_properties(hscrollbar_policy=gtk.POLICY_AUTOMATIC,
                                vscrollbar_policy=gtk.POLICY_AUTOMATIC)
            self.table_model = gtk.ListStore(*([str]*4))
            treeview = gtk.TreeView(self.table_model)
            treeview.show()
            self.add(treeview)

            def add_column(descr, colid):
                column = gtk.TreeViewColumn(descr, gtk.CellRendererText(), text=colid)
                treeview.append_column(column)

            add_column("T"i"m"e"","" ""s""e""l""f"".""C""O""L""U""M""N""_""T""I""M""E"")""
"" "" "" "" "" "" "" "" "" "" "" "" ""a""d""d""_""c""o""l""u""m""n""(