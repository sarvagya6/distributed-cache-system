import os

CONFIG = {
    "CACHE_REPLICATION_FACTOR": int(os.environ.get("CACHE_REPLICATION_FACTOR", 2)),
    "CACHE_NODE_ADDRESSES": os.environ.get(
        "CACHE_NODE_ADDRESSES", "127.0.0.1:8000,127.0.0.1:8001,127.0.0.1:8002"
    ).split(","),
}