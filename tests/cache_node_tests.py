import unittest
from distributed_cache.cache_node.cache import Cache
from distributed_cache.cache_node.storage import Storage
from distributed_cache.cache_node.eviction_policy import LRUEvictionPolicy

class TestCache(unittest.TestCase):
    def setUp(self):
        self.cache = Cache(LRUEvictionPolicy(), Storage())

    def test_set_get(self):
        self.cache.set("key1", "value1")
        self.assertEqual(self.cache.get("key1"), "value1")

    def test_delete(self):
        self.cache.set("key1", "value1")
        self.cache.delete("key1")
        self.assertIsNone(self.cache.get("key1"))

if __name__ == '__main__':
    unittest.main()
