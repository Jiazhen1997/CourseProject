__author__ = 'Danyang'
import logging
import sys


class Solution(object):
    @property
    def logger(self):
        lgr = logging.getLogger(__name__)
        lgr.setLevel(logging.CRITICAL)
        if not lgr.handlers:
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
            lgr.addHandler(ch)
        return lgr

    def solve(self, cipher):
        
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        M, N, matrix, K = cipher

        start = None
        end = None
        for i in xrange(M):
            for j in xrange(N):
                if matrix[i][j] == "M"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""t""a""r""t"" ""="" ""(""i"","" ""j"")""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""m""a""t""r""i""x""[""i""]""[""j""]"" ""=""="" 