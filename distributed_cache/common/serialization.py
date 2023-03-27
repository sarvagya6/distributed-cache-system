import pickle

def serialize(data):
    return pickle.dumps(data)

def deserialize(data):
    return pickle.loads(data)

# if __name__ == "__main__":
#     # Debug code
#     original_data = {"key": "value"}
#     serialized_data = serialize(original_data)
#     deserialized_data = deserialize(serialized_data)

#     print(f"Original data: {original_data}")
#     print(f"Serialized data: {serialized_data}")
#     print(f"Deserialized data: {deserialized_data}")
