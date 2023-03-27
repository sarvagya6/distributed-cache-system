from collections import OrderedDict

class EvictionPolicy:
    def __init__(self):
        pass

    def record_access(self, key):
        raise NotImplementedError

    def evict(self):
        raise NotImplementedError

class LRUEvictionPolicy(EvictionPolicy):
    def __init__(self):
        super().__init__()
        self._cache = OrderedDict()

    def record_access(self, key):
        if key in self._cache:
            self._cache.move_to_end(key)

    def evict(self):
        key, _ = self._cache.popitem(last=False)
        return key

    def add(self, key):
        self._cache[key] = None

    def remove(self, key):
        if key in self._cache:
            del self._cache[key]
