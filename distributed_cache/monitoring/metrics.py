import time

class Monitoring:
    def __init__(self):
        self.start_time = time.time()
        self.get_requests = 0
        self.set_requests = 0
        self.delete_requests = 0
        self.get_success = 0
        self.get_miss = 0
        self.set_success = 0
        self.delete_success = 0

    def increment_get_requests(self):
        self.get_requests += 1

    def increment_set_requests(self):
        self.set_requests += 1

    def increment_delete_requests(self):
        self.delete_requests += 1

    def increment_get_success(self):
        self.get_success += 1

    def increment_get_miss(self):
        self.get_miss += 1

    def increment_set_success(self):
        self.set_success += 1

    def increment_delete_success(self):
        self.delete_success += 1

    def report(self):
        current_time = time.time()
        uptime = current_time - self.start_time

        return {
            "uptime": uptime,
            "get_requests": self.get_requests,
            "set_requests": self.set_requests,
            "delete_requests": self.delete_requests,
            "get_success": self.get_success,
            "get_miss": self.get_miss,
            "set_success": self.set_success,
            "delete_success": self.delete_success
        }
