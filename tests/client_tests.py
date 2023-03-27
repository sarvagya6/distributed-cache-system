import unittest
from distributed_cache.client.partitioning import Partitioner

class TestPartitioner(unittest.TestCase):
    def setUp(self):
        self.nodes = ["http://localhost:5000", "http://localhost:5001", "http://localhost:5002"]
        self.partitioner = Partitioner(self.nodes)

    def test_get_node(self):
        node1 = self.partitioner.get_node("key1")
        node2 = self.partitioner.get_node("key2")
        node3 = self.partitioner.get_node("key3")
        self.assertIn(node1, self.nodes)
        self.assertIn(node2, self.nodes)
        self.assertIn(node3, self.nodes)
