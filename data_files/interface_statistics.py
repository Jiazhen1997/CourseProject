import gtk
import ns.core
import ns.network
from visualizer.base import InformationWindow

NODE_STATISTICS_MEMORY = 10


class StatisticsCollector(object):
    

    class NetDevStats(object):
        __slots__ = ['rxPackets', 'rxBytes', 'txPackets', 'txBytes',
                     'rxPacketRate', 'rxBitRate', 'txPacketRate', 'txBitRate']

    def __init__(self, visualizer):
        self.node_statistics = {} 
        self.visualizer = visualizer

    def simulation_periodic_update(self, viz):
        nodes_statistics = viz.simulation.sim_helper.GetNodesStatistics()
        for stats in nodes_statistics:
            try:
                raw_stats_list = self.node_statistics[stats.nodeId]
            except KeyError:
                raw_stats_list = []
                self.node_statistics[stats.nodeId] = raw_stats_list
            raw_stats_list.append(stats.statistics)
            while len(raw_stats_list) > NODE_STATISTICS_MEMORY:
                raw_stats_list.pop(0)

    def get_interface_statistics(self, nodeId):
        try:
            raw_stats_list = self.node_statistics[nodeId]
        except KeyError:
            return []
        
        if len(raw_stats_list) < NODE_STATISTICS_MEMORY:
            return []
        assert len(raw_stats_list) == NODE_STATISTICS_MEMORY
        tx_packets1 = [] 
        rx_packets1 = []
        tx_bytes1 = []
        rx_bytes1 = []
        for iface, stats in enumerate(raw_stats_list[0]):
            tx_packets1.append(stats.transmittedPackets)
            tx_bytes1.append(stats.transmittedBytes)
            rx_packets1.append(stats.receivedPackets)
            rx_bytes1.append(stats.receivedBytes)

        retval = []

        k = self.visualizer.sample_period*(NODE_STATISTICS_MEMORY-1)
        for iface, stats in enumerate(raw_stats_list[-1]):
            outStat = self.NetDevStats()
            outStat.txPackets = stats.transmittedPackets
            outStat.txBytes = stats.transmittedBytes
            outStat.rxPackets = stats.receivedPackets
            outStat.rxBytes = stats.receivedBytes
            
            outStat.txPacketRate = (stats.transmittedPackets - tx_packets1[iface])/k
            outStat.rxPacketRate = (stats.receivedPackets - rx_packets1[iface])/k
            outStat.txBitRate = (stats.transmittedBytes - tx_bytes1[iface])*8/k
            outStat.rxBitRate = (stats.receivedBytes - rx_bytes1[iface])*8/k
            retval.append(outStat)
        return retval


class ShowInterfaceStatistics(InformationWindow):
    (
        COLUMN_INTERFACE,

        COLUMN_TX_PACKETS,
        COLUMN_TX_BYTES,
        COLUMN_TX_PACKET_RATE,
        COLUMN_TX_BIT_RATE,

        COLUMN_RX_PACKETS,
        COLUMN_RX_BYTES,
        COLUMN_RX_PACKET_RATE,
        COLUMN_RX_BIT_RATE,

        ) = range(9)

    def __init__(self, visualizer, node_index, statistics_collector):
        InformationWindow.__init__(self)
        self.win = gtk.Dialog(parent=visualizer.window,
                              flags=gtk.DIALOG_DESTROY_WITH_PARENT|gtk.DIALOG_NO_SEPARATOR,
                              buttons=(gtk.STOCK_CLOSE, gtk.RESPONSE_CLOSE))
        self.win.connect("r"e"s"p"o"n"s"e"","" ""s""e""l""f"".""_""r""e""s""p""o""n""s""e""_""c""b"")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""w""i""n"".""s""e""t""_""t""i""t""l""e""(