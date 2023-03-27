# Distributed Cache System

This is a distributed cache system built in Python. The system consists of multiple cache nodes and a client that communicates with the nodes to get, set, and delete key-value pairs.

A low-latency distributed cache system provides a fast, scalable, and fault-tolerant storage solution for temporarily storing and retrieving data. It can be used to speed up applications by caching frequently accessed data, reducing database load and latency. 

Here's an overview of how a distributed cache system works and how it can be used:

1.  **Cache nodes:** The cache system consists of multiple cache nodes, which are responsible for storing and managing data. Each node stores a subset of the data in memory, and the data is distributed across nodes using a partitioning strategy.
    
2.  **Data partitioning:** To distribute data evenly across cache nodes, a partitioning strategy like consistent hashing is used. Consistent hashing assigns each key to a cache node based on a hash function. This approach minimizes data movement when adding or removing nodes and ensures an even distribution of data.
    
3.  **Data replication:** To provide fault tolerance and ensure data consistency, the cache system implements data replication. When a write operation occurs, the data is replicated to multiple nodes. In case of node failures, the system can still serve requests using the replicated data. Replication strategies include primary-replica, quorum, or chain replication.
    
4.  **Cache eviction policies:** Since cache nodes have limited memory, an eviction policy is employed to decide which data to remove when the cache is full. Common eviction policies include Least Recently Used (LRU) and Least Frequently Used (LFU).
    
5.  **Client library:** The distributed cache system provides a client library that applications use to interact with the cache. The library handles communication with cache nodes, data partitioning, and locating the appropriate node for read and write operations.
    
6.  **Usage scenarios:** The distributed cache system can be used in various scenarios, such as:
    
    -   Caching results of database queries or API calls to reduce load on backend systems.
    -   Storing session data in web applications for faster access and load balancing.
    -   Implementing a rate limiter by storing request counts in the cache system.
    -   Using the cache as a temporary storage for data processing pipelines.

## Directory Structure

The project has the following directory structure:

```
distributed_cache/
├── cache_node/
│   ├── __init__.py
│   ├── cache.py
│   ├── eviction_policy.py
│   ├── replication.py
│   └── storage.py
├── client/
│   ├── __init__.py
│   ├── client.py
│   ├── connection.py
│   └── partitioning.py
├── common/
│   ├── __init__.py
│   ├── constants.py
│   ├── hashing.py
│   └── serialization.py
├── config/
│   └── config.py
├── monitoring/
│   ├── __init__.py
│   ├── logging.py
│   └── metrics.py
├── tests/
│   ├── __init__.py
│   ├── cache_node_tests.py
│   ├── client_tests.py
│   └── test_utils.py
├── __init__.py
├── cache_node_server.py
└── test_client.py
```

## Components

### Cache Node

The `cache_node` directory contains the following components:

-   `cache.py`: Cache management class
-   `eviction_policy.py`: Eviction policy classes (currently only LRU) 
-   `replication.py`: Replication management class
-   `storage.py`: In-memory storage class

### Client

The `client` directory contains the following components:

-   `client.py`: Cache client class
-   `connection.py`: Connection management class
-   `partitioning.py`: Data partitioning class (consistent hashing, etc.)

### Common

The `common` directory contains the following components:

-   `constants.py`: Constants used across the project
-   `hashing.py`: Hashing functions
-   `serialization.py`: Serialization and deserialization functions

### Config

The `config` directory contains configuration settings and variables.

### Monitoring

The `monitoring` directory contains functions for logging and metrics collection.

### Tests

The `tests` directory contains unit tests for cache_node and client components, as well as utility functions and classes for tests.

## Usage

To start a single cache node, run this with the desired port number as an argument:

`python -m distributed_cache.cache_node_server 5000` 

To start multiple cache nodes run this:

`python -m distributed_cache.launch_cache_nodes`

This will start server on ports 5000, 5001 and 5002.

## Testing

We can run tests using the following commands:

`python -m unittest tests.cache_node_tests` and `python -m unittest tests.client_tests`

