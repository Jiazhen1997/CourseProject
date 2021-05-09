

from collections import defaultdict, OrderedDict
DUMMY = None


class LFUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.values = {}
        self.freqs = defaultdict(int)
        self.keys = defaultdict(OrderedDict)
        self.mini = -1  

    def get(self, key: int) -> int:
        if key in self.values:
            val = self.values[key]
            freq_org = self.freqs[key]
            self.freqs[key] += 1
            del self.keys[freq_org][key]
            self.keys[freq_org + 1][key] = DUMMY  

            if freq_org == self.mini and len(self.keys[self.mini]) == 0:
                self.mini = freq_org + 1

            return val
        else:
            return - 1

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:  
            return

        if key in self.values:
            self.values[key] = value
            self.get(key)  
        else:
            if len(self.values) >= self.cap:
                evit_key, _ = self.keys[self.mini].popitem(last=False)  
                del self.values[evit_key]
                del self.freqs[evit_key]

            self.values[key] = value
            self.freqs[key] = 0
            self.keys[0][key] = DUMMY
            self.get(key)  
            self.mini = 1






