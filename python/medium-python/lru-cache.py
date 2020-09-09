from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache.keys():
            return -1
        val = self.cache.pop(key)
        self.cache[key] = val
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache.keys():
            self.cache.pop(key)
        else:
            if self.capacity == 0:
                self.cache.popitem(False)
            else:
                self.capacity -= 1
        self.cache[key] = value
        return None
    
