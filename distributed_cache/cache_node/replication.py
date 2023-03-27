import asyncio
from aiohttp import ClientSession

class ReplicationManager:
    def __init__(self, nodes):
        self.nodes = nodes

    async def _replicate_write(self, session, node, key, value):
        url = f"http://{node}/set?key={key}&value={value}"
        async with session.get(url) as response:
            await response.read()

    async def _replicate_delete(self, session, node, key):
        url = f"http://{node}/delete?key={key}"
        async with session.get(url) as response:
            await response.read()

    async def replicate_write(self, key, value):
        async with ClientSession() as session:
            tasks = [self._replicate_write(session, node, key, value) for node in self.nodes]
            await asyncio.gather(*tasks, return_exceptions=True)

    async def replicate_delete(self, key):
        async with ClientSession() as session:
            tasks = [self._replicate_delete(session, node, key) for node in self.nodes]
            await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == "__main__":
    async def main():
        # Debug code
        replication_manager = ReplicationManager(["node1", "node2", "node3"])

        await replication_manager.replicate_write("key1", "value1")
        print("Replicated write operation for key1")

        await replication_manager.replicate_delete("key1")
        print("Replicated delete operation for key1")

    asyncio.run(main())
