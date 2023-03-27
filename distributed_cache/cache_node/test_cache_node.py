import asyncio
from random import randint
from .replication import ReplicationManager
from .cache import Cache
from .storage import Storage
from .eviction_policy import LRUEvictionPolicy

async def simulate_requests(replication_manager, cache_instance, num_requests=100):
    for _ in range(num_requests):
        key = f"key{randint(1, 100)}"
        value = f"value{randint(1, 100)}"

        cache_instance.set(key, value)
        await replication_manager.replicate_write(key, value)

        print(f"Set {key} to {value}")

        if randint(0, 1):
            cache_instance.delete(key)
            await replication_manager.replicate_delete(key)
            print(f"Deleted {key}")

if __name__ == "__main__":
    storage = Storage()
    eviction_policy = LRUEvictionPolicy()
    cache_instance = Cache(eviction_policy, storage)

    replication_manager = ReplicationManager(["localhost:5000", "localhost:5001", "localhost:5002"])

    asyncio.run(simulate_requests(replication_manager, cache_instance))
