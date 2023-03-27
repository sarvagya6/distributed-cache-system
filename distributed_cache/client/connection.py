import requests

class ConnectionManager:
    def __init__(self, nodes):
        self.nodes = nodes

    def send_request(self, node, request):
        url = f"http://{node}/cache"
        method = request["method"]

        if method == "GET":
            response = requests.get(url, params={"key": request["key"]})
        elif method == "SET":
            response = requests.post(url, json={"key": request["key"], "value": request["value"]})
        elif method == "DELETE":
            response = requests.delete(url, params={"key": request["key"]})
        else:
            raise ValueError("Invalid request method")

        return response
