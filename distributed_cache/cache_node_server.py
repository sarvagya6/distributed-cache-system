from flask import Flask, request, jsonify
from distributed_cache.cache_node.cache import Cache
from distributed_cache.monitoring.metrics import Monitoring
from distributed_cache.monitoring.log_handler import LogHandler

app = Flask(__name__)
cache = Cache()
monitoring = Monitoring()
log_handler = LogHandler("CacheServer")

@app.route("/cache", methods=["PUT"])
def set_value():
    key = request.args.get("key")
    value = request.args.get("value")
    cache.set(key, value)
    monitoring.increment_set_requests()
    monitoring.increment_set_success()
    return "OK"

@app.route("/cache", methods=["GET"])
def get_value():
    key = request.args.get("key")
    monitoring.increment_get_requests()
    value = cache.get(key)
    if value:
        monitoring.increment_get_success()
        return jsonify({"key": key, "value": value})
    else:
        monitoring.increment_get_miss()
        return "Not Found", 404

@app.route("/cache", methods=["DELETE"])
def delete_value():
    key = request.args.get("key")
    cache.delete(key)
    monitoring.increment_delete_requests()
    monitoring.increment_delete_success()
    return "OK"

@app.route("/metrics", methods=["GET"])
def metrics():
    return jsonify(monitoring.report())

if __name__ == "__main__":
    log_handler.info("Starting cache server...")
    app.run(port=5000)
