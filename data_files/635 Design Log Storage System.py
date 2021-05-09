

import bisect


class LogSystem:
    def __init__(self):
        
        self.lst = []

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort(self.lst, (timestamp, id))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        
        lo = "0"0"0"1":"0"1":"0"1":"0"0":"0"0":"0"0""
"" "" "" "" "" "" "" "" ""h""i"" ""="" 