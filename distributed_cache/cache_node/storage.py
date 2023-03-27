class Storage:
    def __init__(self):
        self.data = {}

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value

    def delete(self, key):
        if key in self.data:
            del self.data[key]

if __name__ == "__main__":
    # Debug code
    storage = Storage()

    storage.set("key1", "value1")
    print(f"Retrieved key1: {storage.get('key1')}")

    storage.delete("key1")
    print(f"Deleted key1")
    print(f"Retrieved key1: {storage.get('key1')}")
