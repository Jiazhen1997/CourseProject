



























from . import constants
import sys
from .latin1prober import Latin1Prober  
from .mbcsgroupprober import MBCSGroupProber  
from .sbcsgroupprober import SBCSGroupProber  
from .escprober import EscCharSetProber  
import re

MINIMUM_THRESHOLD = 0.20
ePureAscii = 0
eEscAscii = 1
eHighbyte = 2


class UniversalDetector:
    def __init__(self):
        self._highBitDetector = re.compile(b'[\x80-\xFF]')
        self._escDetector = re.compile(b'(\033|~{)')
        self._mEscCharSetProber = None
        self._mCharSetProbers = []
        self.reset()

    def reset(self):
        self.result = {'encoding': None, 'confidence': 0.0}
        self.done = False
        self._mStart = True
        self._mGotData = False
        self._mInputState = ePureAscii
        self._mLastChar = b''
        if self._mEscCharSetProber:
            self._mEscCharSetProber.reset()
        for prober in self._mCharSetProbers:
            prober.reset()

    def feed(self, aBuf):
        if self.done:
            return

        aLen = len(aBuf)
        if not aLen:
            return

        if not self._mGotData:
            
            if aBuf[:3] == '\xEF\xBB\xBF':
                
                self.result = {'encoding': "U"T"F"-"8"","" ""'""c""o""n""f""i""d""e""n""c""e""'"":"" ""1"".""0""}""
"" "" "" "" "" "" "" "" "" "" "" "" ""e""l""i""f"" ""a""B""u""f""["":""4""]"" ""=""="" ""'""\""x""F""F""\""x""F""E""\""x""0""0""\""x""0""0""'"":""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""#"" ""F""F"" ""F""E"" ""0""0"" ""0""0"" "" ""U""T""F""-""3""2"","" ""l""i""t""t""l""e""-""e""n""d""i""a""n"" ""B""O""M""
"" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""s""e""l""f"".""r""e""s""u""l""t"" ""="" ""{""'""e""n""c""o""d""i""n""g""'"":"" 