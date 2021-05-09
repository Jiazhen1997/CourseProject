import unittest
from ns.core import Simulator, Seconds, Config, int64x64_t
import ns.core
import ns.network
import ns.internet
import ns.mobility
import ns.csma


class TestSimulator(unittest.TestCase):

    def testScheduleNow(self):
        def callback(args):
            self._args_received = args
            self._cb_time = Simulator.Now()
        Simulator.Destroy()
        self._args_received = None
        self._cb_time = None
        Simulator.ScheduleNow(callback, "a"r"g"s"")""
"" "" "" "" "" "" "" "" ""S""i""m""u""l""a""t""o""r"".""R""u""n""("")""
"" "" "" "" "" "" "" "" ""s""e""l""f"".""a""s""s""e""r""t""E""q""u""a""l""(""s""e""l""f"".""_""a""r""g""s""_""r""e""c""e""i""v""e""d"","" 