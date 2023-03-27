import subprocess

cache_node_ports = [5000, 5001, 5002]

processes = []

try:
    for port in cache_node_ports:
        process = subprocess.Popen(["python", "-m", "distributed_cache.cache_node_server", str(port)])
        processes.append(process)

    for process in processes:
        process.wait()
except KeyboardInterrupt:
    for process in processes:
        process.terminate()
