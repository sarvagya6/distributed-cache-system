from .storage import Storage
from .eviction_policy import EvictionPolicy

class Cache:
    def __init__(self, eviction_policy=None, storage=None):
        self.eviction_policy = eviction_policy or EvictionPolicy()
        self.storage = storage or Storage()

    def get(self, key):
        value = self.storage.get(key)
        if value is not None:
            self.eviction_policy.record_access(key)
        return value

    def set(self, key, value):
        self.storage.set(key, value)
        self.eviction_policy.record_access(key)

    def delete(self, key):
        self.storage.delete(key)

    def evict(self):
        key_to_evict = self.eviction_policy.evict()
        if key_to_evict is not None:
            self.storage.delete(key_to_evict)

if __name__ == "__main__":
    # Debug code
    cache = Cache()

    cache.set("key1", "value1")
    print(f"Retrieved key1: {cache.get('key1')}")

    cache.evict()
    print(f"Evicted a key")
    print(f"Retrieved key1: {cache.get('key1')}")
