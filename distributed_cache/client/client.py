from requests.exceptions import JSONDecodeError

class CacheClient:
    def __init__(self, partitioner, connection_manager):
        self.partitioner = partitioner
        self.connection_manager = connection_manager

    async def get(self, key):
        node = self.partitioner.get_node(key)
        response = self.connection_manager.send_request(node, {"method": "GET", "key": key})

        if response.status_code == 200:
            try:
                return response.json()
            except JSONDecodeError:
                print(f"Error: Unexpected response from cache node: {response.content}")
        else:
            print(f"Error: Cache node returned status code {response.status_code}")

    async def set(self, key, value):
        node = self.partitioner.get_node(key)
        request = {"method": "SET", "key": key, "value": value}
        response = self.connection_manager.send_request(node, request)
        return response.status_code

    async def delete(self, key):
        node = self.partitioner.get_node(key)
        request = {"method": "DELETE", "key": key}
        response = self.connection_manager.send_request(node, request)
        return response.status_code
