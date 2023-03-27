import hashlib

def hash_function(key):
    return hashlib.md5(key.encode('utf-8')).hexdigest()

# if __name__ == "__main__":
#     # Debug code
#     key = "example_key"
#     hash_value = hash_function(key)
#     print(f"Hash value for '{key}': {hash_value}")
