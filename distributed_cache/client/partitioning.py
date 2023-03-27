import hashlib

class Partitioner:
    def __init__(self, nodes):
        self.nodes = nodes

    def get_node(self, key):
        hash_key = self._hash_key(key)
        node_index = hash_key % len(self.nodes)
        return self.nodes[node_index]

    def _hash_key(self, key):
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)
