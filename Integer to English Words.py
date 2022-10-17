from collections import defaultdict
from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = defaultdict(int) # key frequency
        self.freq = defaultdict(OrderedDict) # frequency OrderedDict
        self.min = 0
        
    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        
        f = self.d[key]
        val = self.freq[f][key]
        self.d[key] += 1
        del self.freq[f][key]
        self.freq[f + 1][key] = val
        
        if f == self.min and not self.freq[f]:
            self.min += 1
        
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.d:
            f = self.d[key]
            self.d[key] += 1
            del self.freq[f][key]
            self.freq[f + 1][key] = value
            if f == self.min and not self.freq[f]:
                self.min += 1
            return
        if len(self.d) == self.capacity:
            k, v = self.freq[self.min].popitem(last = False)
            del self.d[k]
        
        self.min = 1
        self.freq[1][key] = value
        self.d[key] = 1
        
        return